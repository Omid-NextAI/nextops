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


def scalar_model(
    tmp_path: Path, pairs: list[tuple[str, int, Any]], *, tail: bytes = b""
) -> tuple[Path, int, str]:
    """Only deterministic synthetic scalars; no actual 122B metadata is assumed."""
    formats = {
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
    raw = b"GGUF" + struct.pack("<IQQ", 3, 0, len(pairs))
    for key, kind, value in pairs:
        payload = string(value) if kind == 8 else struct.pack("<" + formats[kind], value)
        raw += string(key) + struct.pack("<I", kind) + payload
    raw += tail
    path = tmp_path / "synthetic-scalars.gguf"
    path.write_bytes(raw)
    return path, len(raw), hashlib.sha256(raw).hexdigest()


# Explicit expected upstream names (not generated from the implementation set).
ARCHITECTURE_SCALARS = (
    "context_length",
    "block_count",
    "embedding_length",
    "vocab_size",
    "feed_forward_length",
    "expert_count",
    "expert_used_count",
    "expert_shared_count",
    "expert_feed_forward_length",
    "expert_shared_feed_forward_length",
    "attention.head_count",
    "attention.head_count_kv",
    "attention.key_length",
    "attention.value_length",
    "full_attention_interval",
    "nextn_predict_layers",
    "ssm.conv_kernel",
    "ssm.inner_size",
    "ssm.state_size",
    "ssm.time_step_rank",
    "ssm.group_count",
    "rope.dimension_count",
)
TOKEN_IDS = (
    "bos_token_id",
    "eos_token_id",
    "eot_token_id",
    "eom_token_id",
    "unknown_token_id",
    "seperator_token_id",
    "padding_token_id",
    "mask_token_id",
    "fim_pre_token_id",
    "fim_suf_token_id",
    "fim_mid_token_id",
    "fim_pad_token_id",
    "fim_rep_token_id",
    "fim_sep_token_id",
)
TOKEN_FLAGS = (
    "add_bos_token",
    "add_eos_token",
    "add_sep_token",
    "add_space_prefix",
    "remove_extra_whitespaces",
)


@pytest.mark.parametrize("suffix", ARCHITECTURE_SCALARS)
@pytest.mark.parametrize("value", [0, 17, (1 << 32) - 1])
def test_architecture_dimensions_are_only_observed_bounded_integer_scalars(
    tmp_path: Path, suffix: str, value: int
) -> None:
    key = "qwen35moe." + suffix
    result = module().inspect(*scalar_model(tmp_path, [(key, 4, value)]))
    assert type(result[key]) is int and result[key] == value
    assert "not_complete_shard_set_or_cpu_acceptance" in result["scope"]
    assert "accepted_context_tokens" not in result
    assert "active_parameters" not in result and "kv_cache_bytes" not in result


@pytest.mark.parametrize("suffix", TOKEN_IDS)
@pytest.mark.parametrize("value", [0, 17, (1 << 32) - 1])
def test_exact_special_token_ids_are_bounded_scalars_not_vocab_validation(
    tmp_path: Path, suffix: str, value: int
) -> None:
    key = "tokenizer.ggml." + suffix
    result = module().inspect(*scalar_model(tmp_path, [(key, 4, value)]))
    assert type(result[key]) is int and result[key] == value
    # No vocabulary content/membership or tokenizer execution was established.
    assert "tokenizer.ggml.tokens" not in result and "vocabulary_verified" not in result


@pytest.mark.parametrize("suffix", TOKEN_FLAGS)
@pytest.mark.parametrize("value", [False, True])
def test_tokenizer_flags_are_real_bool_scalars(tmp_path: Path, suffix: str, value: bool) -> None:
    key = "tokenizer.ggml." + suffix
    result = module().inspect(*scalar_model(tmp_path, [(key, 7, value)]))
    assert result[key] is value


@pytest.mark.parametrize(
    "key",
    [
        "qwen35moe.expert_used_count",
        "qwen35moe.attention.key_length",
        "qwen35moe.context_length",
        "tokenizer.ggml.eos_token_id",
    ],
)
@pytest.mark.parametrize(
    "kind,value",
    [
        (8, "17"),
        (7, True),
        (7, False),
        (6, 17.0),
        (12, 17.0),
        (6, float("nan")),
        (12, float("inf")),
        (12, -float("inf")),
        (5, -1),
        (11, -1),
        (10, 1 << 32),
        (10, (1 << 64) - 1),
    ],
)
def test_integer_fields_reject_coercion_nonfinite_negative_and_unbounded_values(
    tmp_path: Path, key: str, kind: int, value: Any
) -> None:
    probe = module()
    with pytest.raises(probe.MetadataError, match="integer scalar type or bound"):
        probe.inspect(*scalar_model(tmp_path, [(key, kind, value)]))


@pytest.mark.parametrize("suffix", TOKEN_FLAGS)
@pytest.mark.parametrize("kind,value", [(4, 0), (4, 1), (8, "true"), (8, "false"), (6, 1.0)])
def test_tokenizer_flags_do_not_coerce_strings_numbers_or_floats(
    tmp_path: Path, suffix: str, kind: int, value: Any
) -> None:
    probe = module()
    with pytest.raises(probe.MetadataError, match="not a boolean scalar"):
        probe.inspect(*scalar_model(tmp_path, [("tokenizer.ggml." + suffix, kind, value)]))


@pytest.mark.parametrize("byte", [2, 3, 127, 255])
def test_noncanonical_boolean_encoding_is_rejected(tmp_path: Path, byte: int) -> None:
    probe = module()
    raw = b"GGUF" + struct.pack("<IQQ", 3, 0, 1)
    raw += string("tokenizer.ggml.add_eos_token") + struct.pack("<IB", 7, byte)
    path = tmp_path / "malformed-bool.gguf"
    path.write_bytes(raw)
    with pytest.raises(probe.MetadataError, match="boolean encoding"):
        probe.inspect(path, len(raw), hashlib.sha256(raw).hexdigest())


@pytest.mark.parametrize(
    "key",
    [
        "qwen35moe.expert_used_count",
        "qwen35moe.expert_feed_forward_length",
        "qwen35moe.attention.head_count",
        "tokenizer.ggml.eos_token_id",
        "tokenizer.ggml.add_bos_token",
    ],
)
def test_selected_array_forms_are_rejected_without_exposing_per_layer_values(
    tmp_path: Path, key: str
) -> None:
    # Upstream can support arrays for some architecture keys. This intentionally
    # remains scalar-only; rejection cannot be relabeled as a scalar observation.
    probe = module()
    raw = b"GGUF" + struct.pack("<IQQ", 3, 0, 1)
    raw += string(key) + struct.pack("<IIQII", 9, 4, 2, 17, 23)
    path = tmp_path / "unsupported-selected-array.gguf"
    path.write_bytes(raw)
    with pytest.raises(probe.MetadataError, match="unsupported metadata type"):
        probe.inspect(path, len(raw), hashlib.sha256(raw).hexdigest())


def test_unselected_token_arrays_and_near_match_keys_remain_unexposed(tmp_path: Path) -> None:
    probe = module()
    arrays = [
        "tokenizer.ggml.tokens",
        "tokenizer.ggml.merges",
        "tokenizer.ggml.scores",
        "qwen35moe.rope.dimension_sections",
        "qwen35moe.attention.recurrent_layers",
    ]
    raw = b"GGUF" + struct.pack("<IQQ", 3, 0, len(arrays) + 1)
    for key in arrays:
        raw += string(key) + struct.pack("<IIQ", 9, 8, 1) + string("must-not-be-exposed")
    raw += (
        string("tokenizer.ggml.separator_token_id")
        + struct.pack("<I", 8)
        + string("wrong-spelling")
    )
    path = tmp_path / "unselected-arrays.gguf"
    path.write_bytes(raw)
    result = probe.inspect(path, len(raw), hashlib.sha256(raw).hexdigest())
    assert not set(arrays) & set(result)
    assert "tokenizer.ggml.separator_token_id" not in result
    assert "must-not-be-exposed" not in repr(result) and "wrong-spelling" not in repr(result)


def test_moe_missing_fields_are_not_filled_from_the_model_name(tmp_path: Path) -> None:
    result = module().inspect(
        *model(
            tmp_path,
            [
                ("general.architecture", "qwen35moe"),
                ("general.name", "Synthetic 122B-A10B fixture"),
            ],
        )
    )
    for suffix in ARCHITECTURE_SCALARS:
        assert "qwen35moe." + suffix not in result
    assert not any(key.startswith("tokenizer.ggml.") for key in result)
    assert "accepted_context_tokens" not in result


def test_new_fields_do_not_bypass_hash_gate_or_parse_tensor_payload(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    probe = module()
    path, size, digest = scalar_model(
        tmp_path, [("qwen35moe.expert_count", 4, 17)], tail=b"UNREAD_TENSOR_FIXTURE" * 100
    )
    calls: list[int] = []
    original_read = probe.Reader.read

    def read(reader: Any, count: int) -> bytes:
        calls.append(reader.stream.tell() + count)
        value = original_read(reader, count)
        assert isinstance(value, bytes)
        return value

    monkeypatch.setattr(probe.Reader, "read", read)
    with pytest.raises(probe.MetadataError, match="SHA-256 mismatch"):
        probe.inspect(path, size, "0" * 64)
    assert calls == []
    result = probe.inspect(path, size, digest)
    assert result["qwen35moe.expert_count"] == 17
    assert max(calls) == size - len(b"UNREAD_TENSOR_FIXTURE" * 100)


@pytest.mark.parametrize("bound,maximum", [("MAX_METADATA_BYTES", 32), ("MAX_STRING", 16)])
def test_added_scalar_validation_keeps_metadata_byte_and_string_bounds(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, bound: str, maximum: int
) -> None:
    probe = module()
    args = scalar_model(tmp_path, [("tokenizer.ggml.eos_token_id", 4, 17)])
    monkeypatch.setattr(probe, bound, maximum)
    with pytest.raises(probe.MetadataError, match="bound"):
        probe.inspect(*args)
