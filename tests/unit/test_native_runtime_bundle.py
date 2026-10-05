"""Synthetic POSIX filesystem simulations; never live root or native execution acceptance."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import stat
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from types import SimpleNamespace
from typing import Any, cast

import pytest
from jsonschema import Draft202012Validator

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import check_native_runtime_bundle as checker  # noqa: E402

RUNTIME_ROOT = "/srv/nextops/releases/llama.cpp-b29c606e"
INVENTORY_PATH = "/root/runtime-review/native.json"
SYNTHETIC_EXECUTABLE = b"Synthetic fixture, not a native executable.\n"


@dataclass
class SyntheticNode:
    inode: int
    mode: int
    gid: int = 0
    uid: int = 0
    links: int = 1
    contents: bytes = b""
    target: str = ""
    changed_ns: int = 1


class SyntheticPosix:
    """FD-relative no-follow simulation, with explicit fake UID/stat and no real OS writes."""

    name = "posix"
    O_RDONLY = 0
    O_NOFOLLOW = 1
    O_DIRECTORY = 2
    O_CLOEXEC = 4
    O_NONBLOCK = 8

    def __init__(self) -> None:
        self.nodes: dict[str, SyntheticNode] = {}
        self.descriptors: dict[int, tuple[str, SyntheticNode, int]] = {}
        self.euid = 0
        self.next_inode = 1
        self.next_descriptor = 100
        self.hook: Callable[[str, str], None] | None = None

    def geteuid(self) -> int:
        return self.euid

    def add(
        self, path: str, mode: int, *, gid: int = 0, contents: bytes = b"", target: str = ""
    ) -> None:
        self.nodes[path] = SyntheticNode(
            self.next_inode, mode, gid, contents=contents, target=target
        )
        self.next_inode += 1

    def _notify(self, event: str, path: str) -> None:
        if self.hook is not None:
            self.hook(event, path)

    def _path(self, path: str, dir_fd: int | None) -> str:
        if dir_fd is None:
            return path
        return str(PurePosixPath(self.descriptors[dir_fd][0]) / path)

    def _metadata(self, node: SyntheticNode) -> os.stat_result:
        # The real Windows UID and permission model must not stand in for Linux verification.
        return cast(
            os.stat_result,
            SimpleNamespace(
                st_dev=1,
                st_ino=node.inode,
                st_mode=node.mode,
                st_uid=node.uid,
                st_gid=node.gid,
                st_nlink=node.links,
                st_size=len(node.target.encode())
                if stat.S_ISLNK(node.mode)
                else len(node.contents),
                st_mtime_ns=node.changed_ns,
                st_ctime_ns=node.changed_ns,
            ),
        )

    def open(self, path: str, flags: int, *, dir_fd: int | None = None) -> int:
        selected = self._path(path, dir_fd)
        self._notify("open", selected)
        node = self.nodes.get(selected)
        if node is None or (flags & self.O_NOFOLLOW and stat.S_ISLNK(node.mode)):
            raise OSError("synthetic missing or no-follow failure")
        if flags & self.O_DIRECTORY and not stat.S_ISDIR(node.mode):
            raise OSError("synthetic not-directory failure")
        descriptor = self.next_descriptor
        self.next_descriptor += 1
        self.descriptors[descriptor] = (selected, node, 0)
        return descriptor

    def close(self, descriptor: int) -> None:
        del self.descriptors[descriptor]

    def fstat(self, descriptor: int) -> os.stat_result:
        path, node, _ = self.descriptors[descriptor]
        self._notify("fstat", path)
        return self._metadata(node)

    def stat(
        self, path: str, *, dir_fd: int | None = None, follow_symlinks: bool = True
    ) -> os.stat_result:
        assert not follow_symlinks, "all production metadata lookups must be no-follow"
        selected = self._path(path, dir_fd)
        self._notify("stat", selected)
        if selected not in self.nodes:
            raise OSError("synthetic missing entry")
        return self._metadata(self.nodes[selected])

    def listdir(self, descriptor: int) -> list[str]:
        path = self.descriptors[descriptor][0]
        self._notify("listdir", path)
        return [
            PurePosixPath(name).name
            for name in self.nodes
            if name != "/" and str(PurePosixPath(name).parent) == path
        ]

    def read(self, descriptor: int, length: int) -> bytes:
        path, node, offset = self.descriptors[descriptor]
        self._notify("read", path)
        data = node.contents[offset : offset + length]
        self.descriptors[descriptor] = (path, node, offset + len(data))
        return data

    def readlink(self, path: str, *, dir_fd: int) -> str:
        selected = self._path(path, dir_fd)
        self._notify("readlink", selected)
        return self.nodes[selected].target


@dataclass
class RuntimeFixture:
    fs: SyntheticPosix
    document: dict[str, Any]

    def sync(self) -> str:
        return self.write(json.dumps(self.document).encode())

    def write(self, contents: bytes) -> str:
        node = self.fs.nodes[INVENTORY_PATH]
        node.contents = contents
        node.changed_ns += 1
        return hashlib.sha256(contents).hexdigest()

    def verify(self) -> checker.VerificationSummary:
        return checker.verify_bundle(INVENTORY_PATH, self.sync())


@pytest.fixture
def runtime_fixture(monkeypatch: pytest.MonkeyPatch) -> RuntimeFixture:
    fs = SyntheticPosix()
    for path in (
        "/",
        "/srv",
        "/srv/nextops",
        "/srv/nextops/releases",
        "/root",
        "/root/runtime-review",
    ):
        fs.add(path, stat.S_IFDIR | 0o755)
    fs.add(RUNTIME_ROOT, stat.S_IFDIR | 0o750, gid=2000)
    fs.add(RUNTIME_ROOT + "/bin", stat.S_IFDIR | 0o750, gid=2000)
    contents = {
        "bin/llama-server": SYNTHETIC_EXECUTABLE,
        "bin/libllama.so.0": b"Synthetic CPU library A.\n",
        "bin/libggml.so.0": b"Synthetic CPU library B.\n",
    }
    files = []
    for path, value in contents.items():
        mode = 0o750 if path == "bin/llama-server" else 0o640
        fs.add(RUNTIME_ROOT + "/" + path, stat.S_IFREG | mode, gid=2000, contents=value)
        files.append(
            {
                "path": path,
                "size_bytes": len(value),
                "mode": f"{mode:04o}",
                "gid": 2000,
                "sha256": checker.BINARY_SHA256
                if path == "bin/llama-server"
                else hashlib.sha256(value).hexdigest(),
            }
        )
    aliases = [
        {"path": "bin/libllama.so", "target": "libllama.so.0", "gid": 2000},
        {"path": "bin/libggml.so", "target": "libggml.so.0", "gid": 2000},
    ]
    for record in aliases:
        fs.add(
            RUNTIME_ROOT + "/" + str(record["path"]),
            stat.S_IFLNK | 0o777,
            gid=2000,
            target=str(record["target"]),
        )
    fs.add(INVENTORY_PATH, stat.S_IFREG | 0o600)
    document: dict[str, Any] = {
        "schema_version": "1.0.0",
        "source_commit": checker.SOURCE_COMMIT,
        "runtime_root": RUNTIME_ROOT,
        "root_mode": "0750",
        "root_gid": 2000,
        "binary_sha256": checker.BINARY_SHA256,
        "directories": [{"path": "bin", "mode": "0750", "gid": 2000}],
        "files": files,
        "aliases": aliases,
    }
    monkeypatch.setattr(checker, "os", fs)
    real_hash_descriptor = checker._hash_descriptor

    def synthetic_executable_identity(descriptor: int, expected_size: int) -> str:
        actual = real_hash_descriptor(descriptor, expected_size)
        # This is an explicit fixture substitution, not a manufactured live SHA-256 proof.
        if actual == hashlib.sha256(SYNTHETIC_EXECUTABLE).hexdigest():
            return checker.BINARY_SHA256
        return actual

    monkeypatch.setattr(checker, "_hash_descriptor", synthetic_executable_identity)
    return RuntimeFixture(fs, document)


def test_synthetic_protected_tree_validates_without_writes_or_leaked_paths(
    runtime_fixture: RuntimeFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    digest = runtime_fixture.sync()
    original = copy.deepcopy(runtime_fixture.fs.nodes)
    assert checker.main(["--inventory", INVENTORY_PATH, "--inventory-sha256", digest]) == 0
    output = capsys.readouterr().out
    assert "files=3; directories=1; aliases=2" in output
    assert "No changes made" in output and "NOT VERIFIED:" in output
    for claim in (
        "effective unit",
        "loaded mappings",
        "ELF closure",
        "CPU execution",
        "deployment",
    ):
        assert claim in output
    assert RUNTIME_ROOT not in output and INVENTORY_PATH not in output and digest not in output
    assert runtime_fixture.fs.nodes == original
    assert not runtime_fixture.fs.descriptors


def test_schema_accepts_the_inventory_and_rejects_an_acceptance_toggle(
    runtime_fixture: RuntimeFixture,
) -> None:
    schema = json.loads(
        (REPOSITORY_ROOT / "deploy/inference/native-runtime-bundle.schema.json").read_text()
    )
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    assert not list(validator.iter_errors(runtime_fixture.document))
    runtime_fixture.document["deployment_approved"] = True
    assert list(validator.iter_errors(runtime_fixture.document))
    with pytest.raises(checker.NativeBundleError, match="strict contract"):
        runtime_fixture.verify()


@pytest.mark.parametrize("digest", ["0" * 64, "A" * 64, "invalid", ""])
def test_external_trust_anchor_is_mandatory(runtime_fixture: RuntimeFixture, digest: str) -> None:
    runtime_fixture.sync()
    with pytest.raises(checker.NativeBundleError, match=r"external|trust anchor"):
        checker.verify_bundle(INVENTORY_PATH, digest)
    assert not runtime_fixture.fs.descriptors


@pytest.mark.parametrize("nested", [False, True])
def test_duplicate_json_fields_are_rejected(runtime_fixture: RuntimeFixture, nested: bool) -> None:
    data = json.dumps(runtime_fixture.document)
    data = (
        data.replace('"gid": 2000', '"gid": 2000, "gid": 2000', 1)
        if nested
        else ('{"schema_version": "1.0.0",' + data[1:])
    )
    digest = runtime_fixture.write(data.encode())
    with pytest.raises(checker.NativeBundleError, match="ambiguous"):
        checker.verify_bundle(INVENTORY_PATH, digest)


@pytest.mark.parametrize(
    "root",
    [
        "/home/developer/build/bin",
        "/srv/nextops/releases/current",
        "/srv/nextops/releases/llama.cpp-deadbeef",
        "/srv/nextops/releases/../llama.cpp-b29c606e",
        "/srv/nextops/releases/llama.cpp-b29c606e/",
        "/srv/nextops/releases/llama.cpp-b29c606e\n",
    ],
)
def test_runtime_root_is_strictly_commit_scoped(runtime_fixture: RuntimeFixture, root: str) -> None:
    runtime_fixture.document["runtime_root"] = root
    with pytest.raises(checker.NativeBundleError, match="protected release scope"):
        runtime_fixture.verify()


@pytest.mark.parametrize(
    "path",
    [
        "../outside",
        "/outside",
        "bin//library",
        "bin/./library",
        "bin/../library",
        "bin\\library",
        "bin/library\n",
        "bin/ space",
        "a/b/c/d/e/f/g/h/i",
    ],
)
def test_unsafe_inventory_paths_are_rejected(runtime_fixture: RuntimeFixture, path: str) -> None:
    runtime_fixture.document["files"][1]["path"] = path
    with pytest.raises(checker.NativeBundleError):
        runtime_fixture.verify()


@pytest.mark.parametrize(
    "field,value",
    [
        ("source_commit", "0" * 40),
        ("binary_sha256", "0" * 64),
        ("schema_version", "2.0.0"),
        ("root_gid", True),
        ("root_gid", 2000.0),
        ("root_mode", "0770"),
    ],
)
def test_pinned_identity_and_strict_types_are_required(
    runtime_fixture: RuntimeFixture, field: str, value: object
) -> None:
    runtime_fixture.document[field] = value
    with pytest.raises(checker.NativeBundleError):
        runtime_fixture.verify()


@pytest.mark.parametrize("target", ["/tmp/library", "../../escape", "missing.so", "libggml.so"])
def test_escaping_dangling_and_cyclic_aliases_are_rejected(
    runtime_fixture: RuntimeFixture, target: str
) -> None:
    runtime_fixture.document["aliases"][1]["target"] = target
    with pytest.raises(checker.NativeBundleError, match="alias"):
        runtime_fixture.verify()


def test_valid_bounded_relative_alias_chain(runtime_fixture: RuntimeFixture) -> None:
    runtime_fixture.document["aliases"][0]["target"] = "libggml.so"
    runtime_fixture.fs.nodes[RUNTIME_ROOT + "/bin/libllama.so"].target = "libggml.so"
    assert runtime_fixture.verify().alias_count == 2


def test_bounded_parent_relative_alias_remains_inside_the_root(
    runtime_fixture: RuntimeFixture,
) -> None:
    runtime_fixture.document["aliases"][0]["target"] = "../bin/libllama.so.0"
    runtime_fixture.fs.nodes[RUNTIME_ROOT + "/bin/libllama.so"].target = "../bin/libllama.so.0"
    assert runtime_fixture.verify().alias_count == 2


def test_alias_parent_cannot_substitute_for_a_directory(runtime_fixture: RuntimeFixture) -> None:
    runtime_fixture.document["files"][1]["path"] = "bin/libggml.so/child"
    with pytest.raises(checker.NativeBundleError, match="parent"):
        runtime_fixture.verify()


@pytest.mark.parametrize("kind", ["files", "aliases", "directories"])
def test_duplicate_inventory_paths_are_rejected(runtime_fixture: RuntimeFixture, kind: str) -> None:
    runtime_fixture.document[kind].append(copy.deepcopy(runtime_fixture.document[kind][0]))
    with pytest.raises(checker.NativeBundleError, match="duplicate"):
        runtime_fixture.verify()


@pytest.mark.parametrize(
    "path",
    [
        "/srv",
        "/srv/nextops",
        "/srv/nextops/releases",
        RUNTIME_ROOT,
        RUNTIME_ROOT + "/bin",
        "/root/runtime-review",
    ],
)
def test_raw_root_and_inventory_ancestors_cannot_be_symlinks(
    runtime_fixture: RuntimeFixture, path: str
) -> None:
    runtime_fixture.fs.nodes[path].mode = stat.S_IFLNK | 0o777
    with pytest.raises(checker.NativeBundleError, match="object type"):
        runtime_fixture.verify()
    assert not runtime_fixture.fs.descriptors


@pytest.mark.parametrize(
    "path",
    [
        "/srv/nextops/releases",
        RUNTIME_ROOT,
        RUNTIME_ROOT + "/bin",
        RUNTIME_ROOT + "/bin/libllama.so.0",
        RUNTIME_ROOT + "/bin/libllama.so",
        INVENTORY_PATH,
    ],
)
def test_all_objects_and_ancestors_must_be_root_owned(
    runtime_fixture: RuntimeFixture, path: str
) -> None:
    runtime_fixture.fs.nodes[path].uid = 1000
    with pytest.raises(checker.NativeBundleError, match="root owned"):
        runtime_fixture.verify()


@pytest.mark.parametrize("bits", [0o020, 0o002, 0o4000, 0o2000, 0o1000])
@pytest.mark.parametrize("path", ["/srv/nextops/releases", RUNTIME_ROOT + "/bin/llama-server"])
def test_unsafe_permissions_are_rejected(
    runtime_fixture: RuntimeFixture, bits: int, path: str
) -> None:
    runtime_fixture.fs.nodes[path].mode |= bits
    with pytest.raises(checker.NativeBundleError, match="unsafe write or special"):
        runtime_fixture.verify()


@pytest.mark.parametrize(
    "path", [INVENTORY_PATH, RUNTIME_ROOT + "/bin/libggml.so.0", RUNTIME_ROOT + "/bin/libggml.so"]
)
def test_hardlinks_are_rejected(runtime_fixture: RuntimeFixture, path: str) -> None:
    runtime_fixture.fs.nodes[path].links = 2
    with pytest.raises(checker.NativeBundleError, match="hard-linked"):
        runtime_fixture.verify()


@pytest.mark.parametrize("kind", [stat.S_IFIFO, stat.S_IFCHR, stat.S_IFSOCK, stat.S_IFLNK])
def test_special_files_are_never_opened_or_executed(
    runtime_fixture: RuntimeFixture, kind: int
) -> None:
    path = RUNTIME_ROOT + "/bin/libggml.so.0"
    runtime_fixture.fs.nodes[path].mode = kind | 0o640
    with pytest.raises(checker.NativeBundleError, match="object type"):
        runtime_fixture.verify()


@pytest.mark.parametrize("mutation", ["digest", "size", "gid", "mode", "binary_digest"])
def test_corrupt_or_changed_regular_files_fail_closed(
    runtime_fixture: RuntimeFixture, mutation: str
) -> None:
    path = RUNTIME_ROOT + (
        "/bin/llama-server" if mutation == "binary_digest" else "/bin/libggml.so.0"
    )
    node = runtime_fixture.fs.nodes[path]
    if mutation in {"digest", "binary_digest"}:
        node.contents = b"X" + node.contents[1:]
    elif mutation == "size":
        node.contents += b"X"
    elif mutation == "gid":
        node.gid = 0
    else:
        node.mode = stat.S_IFREG | 0o600
    with pytest.raises(checker.NativeBundleError, match=r"digest mismatch|metadata differs"):
        runtime_fixture.verify()


@pytest.mark.parametrize("mutation", ["missing", "extra", "alias"])
def test_inventory_is_an_exact_file_and_alias_set(
    runtime_fixture: RuntimeFixture, mutation: str
) -> None:
    if mutation == "missing":
        del runtime_fixture.fs.nodes[RUNTIME_ROOT + "/bin/libggml.so.0"]
    elif mutation == "extra":
        runtime_fixture.fs.add(RUNTIME_ROOT + "/bin/unlisted", stat.S_IFREG | 0o640)
    else:
        runtime_fixture.fs.nodes[RUNTIME_ROOT + "/bin/libggml.so"].target = "libllama.so.0"
    with pytest.raises(checker.NativeBundleError, match=r"missing|unlisted|alias identity"):
        runtime_fixture.verify()


@pytest.mark.parametrize("bound", ["inventory", "file", "count", "total"])
def test_inventory_and_hash_work_are_bounded(runtime_fixture: RuntimeFixture, bound: str) -> None:
    if bound == "inventory":
        digest = runtime_fixture.write(b"X" * (checker.MAX_INVENTORY_BYTES + 1))
        with pytest.raises(checker.NativeBundleError, match="size exceeds"):
            checker.verify_bundle(INVENTORY_PATH, digest)
        return
    if bound == "file":
        runtime_fixture.document["files"][1]["size_bytes"] = checker.MAX_FILE_BYTES + 1
    elif bound == "count":
        runtime_fixture.document["aliases"] *= checker.MAX_ALIASES
    else:
        for index in range(5):
            record = copy.deepcopy(runtime_fixture.document["files"][1])
            record.update(path=f"bin/large-{index}", size_bytes=checker.MAX_FILE_BYTES)
            runtime_fixture.document["files"].append(record)
    with pytest.raises(checker.NativeBundleError, match="bound"):
        runtime_fixture.verify()


def test_file_metadata_change_during_hashing_is_rejected(runtime_fixture: RuntimeFixture) -> None:
    path = RUNTIME_ROOT + "/bin/libggml.so.0"

    def change(event: str, selected: str) -> None:
        if event == "read" and selected == path:
            runtime_fixture.fs.hook = None
            runtime_fixture.fs.nodes[path].changed_ns += 1

    runtime_fixture.fs.hook = change
    with pytest.raises(checker.NativeBundleError, match="metadata changed"):
        runtime_fixture.verify()
    assert not runtime_fixture.fs.descriptors


def test_inode_swap_between_lstat_and_open_is_rejected(runtime_fixture: RuntimeFixture) -> None:
    path = RUNTIME_ROOT + "/bin/libggml.so.0"

    def swap(event: str, selected: str) -> None:
        if event == "open" and selected == path:
            runtime_fixture.fs.hook = None
            runtime_fixture.fs.nodes[path].inode += 100

    runtime_fixture.fs.hook = swap
    with pytest.raises(checker.NativeBundleError, match="changed before verification"):
        runtime_fixture.verify()
    assert not runtime_fixture.fs.descriptors


def test_alias_swap_during_readlink_is_rejected(runtime_fixture: RuntimeFixture) -> None:
    path = RUNTIME_ROOT + "/bin/libggml.so"

    def swap(event: str, selected: str) -> None:
        if event == "readlink" and selected == path:
            runtime_fixture.fs.hook = None
            runtime_fixture.fs.nodes[path].inode += 100

    runtime_fixture.fs.hook = swap
    with pytest.raises(checker.NativeBundleError, match="alias metadata changed"):
        runtime_fixture.verify()
    assert not runtime_fixture.fs.descriptors


def test_inventory_leaf_symlink_is_rejected(runtime_fixture: RuntimeFixture) -> None:
    runtime_fixture.fs.nodes[INVENTORY_PATH].mode = stat.S_IFLNK | 0o777
    with pytest.raises(checker.NativeBundleError, match="object type"):
        runtime_fixture.verify()
    assert not runtime_fixture.fs.descriptors


def test_actual_tree_enumeration_has_a_separate_bound(runtime_fixture: RuntimeFixture) -> None:
    for index in range(checker.MAX_TREE_ENTRIES + 1):
        runtime_fixture.fs.add(RUNTIME_ROOT + f"/bin/extra-{index}", stat.S_IFREG | 0o640)
    with pytest.raises(checker.NativeBundleError, match="tree entry count"):
        runtime_fixture.verify()
    assert not runtime_fixture.fs.descriptors


@pytest.mark.parametrize("target", ["tree", "inventory"])
def test_final_stability_check_rejects_changes_between_scans(
    runtime_fixture: RuntimeFixture, monkeypatch: pytest.MonkeyPatch, target: str
) -> None:
    original = checker._scan_tree

    def change(
        inventory: checker.Inventory, *, verify_hashes: bool
    ) -> dict[str, checker.Fingerprint | str]:
        result = original(inventory, verify_hashes=verify_hashes)
        if verify_hashes:
            selected = RUNTIME_ROOT + "/bin" if target == "tree" else INVENTORY_PATH
            runtime_fixture.fs.nodes[selected].changed_ns += 1
        return result

    monkeypatch.setattr(checker, "_scan_tree", change)
    with pytest.raises(checker.NativeBundleError, match="metadata changed"):
        runtime_fixture.verify()


@pytest.mark.parametrize("platform,euid", [("nt", 0), ("posix", 1000)])
def test_cli_never_uses_windows_or_nonroot_as_a_live_bypass(
    runtime_fixture: RuntimeFixture, capsys: pytest.CaptureFixture[str], platform: str, euid: int
) -> None:
    runtime_fixture.fs.name = platform
    runtime_fixture.fs.euid = euid
    assert (
        checker.main(
            [
                "--inventory",
                INVENTORY_PATH,
                "--inventory-sha256",
                runtime_fixture.sync(),
            ]
        )
        == 1
    )
    output = capsys.readouterr()
    assert "requires POSIX root" in output.err and not output.out
    assert INVENTORY_PATH not in output.err and not runtime_fixture.fs.descriptors


def test_cli_has_no_apply_execution_or_acceptance_options(runtime_fixture: RuntimeFixture) -> None:
    with pytest.raises(SystemExit) as failure:
        checker.main(
            [
                "--inventory",
                INVENTORY_PATH,
                "--inventory-sha256",
                runtime_fixture.sync(),
                "--apply",
            ]
        )
    assert failure.value.code == 2
