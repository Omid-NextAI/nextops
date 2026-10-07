"""Inspect bounded GGUF metadata offline, without loading tensors or emitting templates."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path
from typing import Any, BinaryIO

# Exact scalar keys from llama.cpp b29c606e's gguf/constants.py and GGUF writer.
# These are inspection bounds, not model compatibility, active-parameter, KV
# allocation or usable-context validation. Missing fields stay absent.
TOKEN_ID_FIELDS = {
    "tokenizer.ggml.bos_token_id",
    "tokenizer.ggml.eos_token_id",
    "tokenizer.ggml.eot_token_id",
    "tokenizer.ggml.eom_token_id",
    "tokenizer.ggml.unknown_token_id",
    "tokenizer.ggml.seperator_token_id",  # Upstream spelling, not a corrected alias.
    "tokenizer.ggml.padding_token_id",
    "tokenizer.ggml.mask_token_id",
    "tokenizer.ggml.fim_pre_token_id",
    "tokenizer.ggml.fim_suf_token_id",
    "tokenizer.ggml.fim_mid_token_id",
    "tokenizer.ggml.fim_pad_token_id",
    "tokenizer.ggml.fim_rep_token_id",
    "tokenizer.ggml.fim_sep_token_id",
}
TOKEN_FLAG_FIELDS = {
    "tokenizer.ggml.add_bos_token",
    "tokenizer.ggml.add_eos_token",
    "tokenizer.ggml.add_sep_token",
    "tokenizer.ggml.add_space_prefix",
    "tokenizer.ggml.remove_extra_whitespaces",
}
ARCHITECTURE_INTEGER_SUFFIXES = (
    ".context_length",
    ".block_count",
    ".embedding_length",
    ".vocab_size",
    ".feed_forward_length",
    ".expert_count",
    ".expert_used_count",
    ".expert_shared_count",
    ".expert_feed_forward_length",
    ".expert_shared_feed_forward_length",
    ".attention.head_count",
    ".attention.head_count_kv",
    ".attention.key_length",
    ".attention.value_length",
    ".full_attention_interval",
    ".nextn_predict_layers",
    ".ssm.conv_kernel",
    ".ssm.inner_size",
    ".ssm.state_size",
    ".ssm.time_step_rank",
    ".ssm.group_count",
    ".rope.dimension_count",
)
MAX_SCALAR_UINT = (1 << 32) - 1
FIELDS = (
    {
        "general.architecture",
        "general.name",
        "general.file_type",
        "general.quantization_version",
        "general.license",
        "general.size_label",
        "general.base_model.0.name",
        "general.base_model.0.repo_url",
        "tokenizer.ggml.model",
        "tokenizer.ggml.pre",
        "tokenizer.chat_template",
        "split.no",
        "split.count",
        "split.tensors.count",
    }
    | TOKEN_ID_FIELDS
    | TOKEN_FLAG_FIELDS
)
FORMATS = {
    0: "B",
    1: "b",
    2: "H",
    3: "h",
    4: "I",
    5: "i",
    6: "f",
    7: "?",
    10: "Q",
    11: "q",
    12: "d",
}
MAX_STRING = 16_777_216
MAX_METADATA_BYTES = 134_217_728


class MetadataError(ValueError):
    """Untrusted model metadata failed a bound, identity or format check."""


class Reader:
    def __init__(self, stream: BinaryIO, size: int) -> None:
        self.stream = stream
        self.limit = min(size, MAX_METADATA_BYTES)

    def read(self, size: int) -> bytes:
        if not 0 <= size <= MAX_STRING or self.stream.tell() + size > self.limit:
            raise MetadataError("metadata byte bound exceeded")
        value = self.stream.read(size)
        if len(value) != size:
            raise MetadataError("truncated metadata")
        return value

    def number(self, fmt: str) -> Any:
        return struct.unpack("<" + fmt, self.read(struct.calcsize("<" + fmt)))[0]

    def skip(self, size: int) -> None:
        if size < 0 or self.stream.tell() + size > self.limit:
            raise MetadataError("metadata skip bound exceeded")
        self.stream.seek(size, 1)

    def string(self, capture: bool) -> str | None:
        size = self.number("Q")
        if size > MAX_STRING:
            raise MetadataError("metadata string bound exceeded")
        if capture:
            try:
                return self.read(size).decode("utf-8")
            except UnicodeError as error:
                raise MetadataError("invalid UTF-8 metadata") from error
        self.skip(size)
        return None

    def value(self, kind: int, capture: bool) -> Any:
        if kind == 7:
            value = self.number("B")
            if value not in (0, 1):
                raise MetadataError("invalid metadata boolean encoding")
            return bool(value)
        if kind in FORMATS:
            return self.number(FORMATS[kind])
        if kind == 8:
            return self.string(capture)
        if kind != 9 or capture:
            raise MetadataError("unsupported metadata type")
        child, count = self.number("I"), self.number("Q")
        if count > 10_000_000 or child not in {*FORMATS, 8}:
            raise MetadataError("metadata array bound or type invalid")
        if child in FORMATS:
            self.skip(struct.calcsize("<" + FORMATS[child]) * count)
        else:
            for _ in range(count):
                self.string(False)
        return None


def inspect(path: Path, expected_size: int, expected_sha256: str) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file() or path.stat().st_size != expected_size:
        raise MetadataError("model must be a regular exact-size file")
    if len(expected_sha256) != 64 or any(c not in "0123456789abcdef" for c in expected_sha256):
        raise MetadataError("expected SHA-256 is invalid")
    with path.open("rb") as stream:
        if hashlib.file_digest(stream, "sha256").hexdigest() != expected_sha256:
            raise MetadataError("model SHA-256 mismatch")
        stream.seek(0)
        reader = Reader(stream, expected_size)
        if reader.read(4) != b"GGUF":
            raise MetadataError("not GGUF")
        version, tensors, metadata = reader.number("I"), reader.number("Q"), reader.number("Q")
        if version != 3 or metadata > 10_000:
            raise MetadataError("GGUF version or metadata count unsupported")
        result: dict[str, Any] = {"gguf_version": version, "tensor_count": tensors}
        seen: set[str] = set()
        for _ in range(metadata):
            key = reader.string(True)
            if key is None or key in seen:
                raise MetadataError("duplicate metadata key")
            seen.add(key)
            architecture_integer = key.endswith(ARCHITECTURE_INTEGER_SUFFIXES)
            capture = key in FIELDS or architecture_integer
            value = reader.value(reader.number("I"), capture)
            if capture:
                if architecture_integer or key in TOKEN_ID_FIELDS:
                    if type(value) is not int or not 0 <= value <= MAX_SCALAR_UINT:
                        raise MetadataError("metadata integer scalar type or bound invalid")
                elif key in TOKEN_FLAG_FIELDS and type(value) is not bool:
                    raise MetadataError("tokenizer flag is not a boolean scalar")
                if key == "tokenizer.chat_template":
                    if not isinstance(value, str):
                        raise MetadataError("chat template is not a string")
                    result["chat_template_sha256"] = hashlib.sha256(value.encode()).hexdigest()
                else:
                    result[key] = value
        result["metadata_count"] = metadata
        result["scope"] = "verified_file_metadata_not_complete_shard_set_or_cpu_acceptance"
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--expected-size", type=int, required=True)
    parser.add_argument("--expected-sha256", required=True)
    args = parser.parse_args()
    try:
        result = inspect(args.model, args.expected_size, args.expected_sha256)
    except (OSError, MetadataError) as error:
        parser.exit(1, f"FAIL: {error}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
