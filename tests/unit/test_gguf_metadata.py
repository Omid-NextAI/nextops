"""Synthetic metadata tests are not actual model-loading acceptance."""

from __future__ import annotations

import hashlib
import importlib.util
import struct
from pathlib import Path
from typing import Any

import pytest


def module() -> Any:
    spec = importlib.util.spec_from_file_location(
        "metadata_probe", Path(__file__).resolve().parents[2] / "scripts/inspect_gguf_metadata.py"
    )
    assert spec and spec.loader
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def string(value: str) -> bytes:
    raw = value.encode()
    return struct.pack("<Q", len(raw)) + raw


def model(tmp_path: Path, pairs: list[tuple[str, str]]) -> tuple[Path, int, str]:
    raw = b"GGUF" + struct.pack("<IQQ", 3, 0, len(pairs))
    raw += b"".join(string(k) + struct.pack("<I", 8) + string(v) for k, v in pairs)
    path = tmp_path / "synthetic.gguf"
    path.write_bytes(raw)
    return path, len(raw), hashlib.sha256(raw).hexdigest()


def test_inspection_hashes_template_instead_of_emitting_it(tmp_path: Path) -> None:
    args = model(
        tmp_path,
        [("general.architecture", "qwen4exp"), ("tokenizer.chat_template", "private-template")],
    )
    result = module().inspect(*args)
    assert result["general.architecture"] == "qwen4exp"
    assert result["chat_template_sha256"] == hashlib.sha256(b"private-template").hexdigest()
    assert "tokenizer.chat_template" not in result
    assert "not_complete_shard_set" in result["scope"]


def test_duplicate_metadata_is_rejected(tmp_path: Path) -> None:
    probe = module()
    with pytest.raises(probe.MetadataError, match="duplicate"):
        probe.inspect(
            *model(tmp_path, [("general.architecture", "a"), ("general.architecture", "b")])
        )


def test_exact_size_and_sha_are_required(tmp_path: Path) -> None:
    probe = module()
    path, size, digest = model(tmp_path, [])
    with pytest.raises(probe.MetadataError, match="exact-size"):
        probe.inspect(path, size + 1, digest)
    with pytest.raises(probe.MetadataError, match="SHA-256 mismatch"):
        probe.inspect(path, size, "0" * 64)


@pytest.mark.parametrize("kind,count", [(9, 1), (8, 10_000_001), (4, 10_000_000)])
def test_nested_excessive_or_truncated_arrays_are_rejected(
    tmp_path: Path, kind: int, count: int
) -> None:
    probe = module()
    raw = b"GGUF" + struct.pack("<IQQ", 3, 0, 1)
    raw += string("tokenizer.ggml.tokens") + struct.pack("<IIQ", 9, kind, count)
    path = tmp_path / "malformed.gguf"
    path.write_bytes(raw)
    with pytest.raises(probe.MetadataError, match=r"bound|invalid"):
        probe.inspect(path, len(raw), hashlib.sha256(raw).hexdigest())
