"""Offline equivalence and safety bounds for application-code digest evidence."""

import os
import warnings
from pathlib import Path
from zipfile import ZipFile

import pytest

from nextops.api.release_identity import CodeDigestError, installed_code_digest, wheel_code_digest


def _fixture(tmp_path: Path, *, duplicate: bool = False) -> tuple[Path, Path]:
    root = tmp_path / "nextops"
    (root / "api" / "static").mkdir(parents=True)
    (root / "api" / "app.py").write_text("value = 1\n", encoding="utf-8")
    (root / "api" / "static" / "index.html").write_text("<main>local</main>", encoding="utf-8")
    wheel = tmp_path / "nextops-0.1.0-py3-none-any.whl"
    with ZipFile(wheel, "w") as archive:
        for path in sorted(root.rglob("*")):
            if path.is_file():
                archive.write(path, "nextops/" + path.relative_to(root).as_posix())
        if duplicate:
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", message="Duplicate name: 'nextops/api/app.py'")
                archive.writestr("nextops/api/app.py", "value = 2\n")
    return root, wheel


def test_wheel_and_installed_package_digest_match_and_detect_content_change(tmp_path: Path) -> None:
    root, wheel = _fixture(tmp_path)
    expected = wheel_code_digest(wheel)
    assert len(expected) == 64
    assert installed_code_digest(root) == expected

    (root / "api" / "__pycache__").mkdir()
    (root / "api" / "__pycache__" / "app.pyc").write_bytes(b"local cache")
    assert installed_code_digest(root) == expected

    (root / "api" / "app.py").write_text("value = 2\n", encoding="utf-8")
    assert installed_code_digest(root) != expected


def test_wheel_digest_rejects_ambiguous_or_missing_package_members(tmp_path: Path) -> None:
    root, wheel = _fixture(tmp_path, duplicate=True)
    with pytest.raises(CodeDigestError, match="duplicate"):
        wheel_code_digest(wheel)
    (root / "api" / "static" / "index.html").unlink()
    with pytest.raises(CodeDigestError, match="missing"):
        installed_code_digest(root)


def test_wheel_digest_rejects_oversized_and_unreadable_artifacts(tmp_path: Path) -> None:
    _, wheel = _fixture(tmp_path)
    with ZipFile(wheel, "a") as archive:
        archive.writestr("nextops/api/oversized.bin", b"x" * 5_000_001)
    with pytest.raises(CodeDigestError, match="read budget"):
        wheel_code_digest(wheel)
    invalid = tmp_path / "invalid.whl"
    invalid.write_bytes(b"not a wheel")
    with pytest.raises(CodeDigestError, match="cannot be read"):
        wheel_code_digest(invalid)


def test_wheel_digest_rejects_noncanonical_package_paths(tmp_path: Path) -> None:
    _, wheel = _fixture(tmp_path)
    with ZipFile(wheel, "a") as archive:
        archive.writestr("nextops/api/../unexpected.py", "value = 3\n")
    with pytest.raises(CodeDigestError, match="name"):
        wheel_code_digest(wheel)


@pytest.mark.skipif(os.name != "posix", reason="symlink qualification runs on POSIX CI")
def test_installed_digest_rejects_a_linked_package_file(tmp_path: Path) -> None:
    root, _ = _fixture(tmp_path)
    (root / "api" / "linked.py").symlink_to(root / "api" / "app.py")
    with pytest.raises(CodeDigestError, match="linked"):
        installed_code_digest(root)
