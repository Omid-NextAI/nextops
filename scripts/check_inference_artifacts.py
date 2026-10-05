"""Validate pinned, human-readable local-inference candidate metadata."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode

EXPECTED_MANIFEST = "qwen3-8b-q4-k-m.yaml"
LARGER_CANDIDATE = "qwen3-14b-q4-k-m.candidate.json"
LARGER_32B_CANDIDATE = "qwen3-32b-q4-k-m.candidate.json"
LARGER_MOE_CANDIDATE = "qwen3-30b-a3b-q4-k-m.candidate.json"
LARGER_QWEN35_CANDIDATE = "qwen3-5-35b-a3b-q4-k-m.candidate.json"


class ArtifactValidationError(RuntimeError):
    """Raised when candidate metadata is ambiguous or violates its contract."""


class UniqueKeySafeLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of accepting last-value-wins input."""

    def construct_mapping(self, node: MappingNode, deep: bool = False) -> dict[Any, Any]:
        mapping: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in mapping
            except TypeError as error:
                raise ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found unhashable key {key!r}",
                    key_node.start_mark,
                ) from error
            if duplicate:
                raise ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key {key!r}",
                    key_node.start_mark,
                )
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


def _format_path(parts: Any) -> str:
    rendered = ".".join(str(part) for part in parts)
    return rendered or "<root>"


def _unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate artifact metadata field")
        result[key] = value
    return result


def validate_repository(repository_root: Path) -> dict[str, Any]:
    """Validate the exact candidate set and its immutable source metadata."""

    directory = repository_root / "deploy" / "inference"
    schema_path = directory / "inference-artifact.schema.json"
    manifests = {path.name for path in directory.glob("*.yaml")}
    if manifests != {EXPECTED_MANIFEST}:
        raise ArtifactValidationError(
            "candidate manifest set mismatch: "
            f"expected={[EXPECTED_MANIFEST]}, actual={sorted(manifests)}"
        )
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        document = yaml.load(
            (directory / EXPECTED_MANIFEST).read_text(encoding="utf-8"),
            Loader=UniqueKeySafeLoader,
        )
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as error:
        raise ArtifactValidationError(f"cannot parse candidate metadata: {error}") from error
    if not isinstance(document, dict):
        raise ArtifactValidationError("candidate manifest must be a mapping")
    errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(document),
        key=lambda error: list(error.path),
    )
    if errors:
        details = "; ".join(f"{_format_path(error.path)}: {error.message}" for error in errors)
        raise ArtifactValidationError(f"candidate schema validation failed: {details}")
    for candidate_name, schema_name in (
        (LARGER_CANDIDATE, "model-candidate.schema.json"),
        (LARGER_32B_CANDIDATE, "model-32b-candidate.schema.json"),
        (LARGER_MOE_CANDIDATE, "model-30b-a3b-candidate.schema.json"),
        (LARGER_QWEN35_CANDIDATE, "model-35b-a3b-candidate.schema.json"),
        ("qwen3-8-flash-next-q8.candidate.json", "model-flash-next-candidate.schema.json"),
        ("qwen3-5-122b-a10b-q5-k-m.candidate.json", "model-122b-a10b-q5-candidate.schema.json"),
    ):
        try:
            larger_schema = json.loads((directory / schema_name).read_text("utf-8"))
            larger = json.loads(
                (directory / candidate_name).read_text("utf-8"),
                object_pairs_hook=_unique_json_object,
            )
            Draft202012Validator.check_schema(larger_schema)
        except (OSError, ValueError) as error:
            raise ArtifactValidationError(
                f"cannot parse larger candidate metadata: {error}"
            ) from error
        larger_errors = list(Draft202012Validator(larger_schema).iter_errors(larger))
        if larger_errors:
            details = "; ".join(
                f"{_format_path(error.path)}: {error.message}" for error in larger_errors
            )
            raise ArtifactValidationError(f"larger candidate schema validation failed: {details}")
    validate_chat_candidates(directory)
    validate_qwen38_candidate(directory)
    validate_qwen38_q5_candidate(directory)
    return document


def validate_qwen38_q5_candidate(directory: Path) -> None:
    """A distinct smaller-precision experiment cannot inherit Q8 or live acceptance."""
    try:
        candidate = json.loads(
            (directory / "qwen3-8-27b-ud-q5-k-m.candidate.json").read_text("utf-8"),
            object_pairs_hook=_unique_json_object,
        )
    except (OSError, ValueError) as error:
        raise ArtifactValidationError("cannot parse Qwen3.8 Q5 candidate metadata") from error
    expected = {
        "schema_version": "1.0.0",
        "model_id": "nextops-qwen3-8-27b-ud-q5-k-m",
        "source_repository": "https://huggingface.co/unsloth/Qwen3.8-27B-GGUF",
        "source_revision": "4ca720788d1e01f1bff70c033e0d0028fd02e502",
        "upstream_repository": "https://huggingface.co/Qwen/Qwen3.8-27B",
        "upstream_reference_revision": "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0",
        "conversion_source_revision_verified": False,
        "quantized_by": "unsloth",
        "quantization": "UD-Q5_K_M",
        "filename": "Qwen3.8-27B-UD-Q5_K_M.gguf",
        "size_bytes": 19771509664,
        "sha256": "2de73110cb254cbf09b54b717578dadff12ef1194e7271527e68202f39ba4bfd",
        "license": "Apache-2.0",
        "license_size_bytes": 11544,
        "license_sha256": "bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a",
        "runtime_commit": "b29c606e28a01b1bc8c1351026a0fa6e616bf6c4",
        "cpu_only_required": True,
        "gpu_layers": 0,
        "runtime_download_allowed": False,
        "deployment_selection_allowed": False,
        "public_thinking_enabled": False,
        "private_reasoning_persisted": False,
        "configured_context_tokens": 16384,
        "max_output_tokens": 2048,
        "request_reasoning_budget_tokens": 128,
        "deadline_seconds": 120,
        "max_active_requests": 1,
        "max_queued_requests": 2,
    }
    if not isinstance(candidate, dict) or set(candidate) != {*expected, "status", "qualification"}:
        raise ArtifactValidationError("Qwen3.8 Q5 metadata fields changed")
    if any(
        type(candidate[key]) is not type(value) or candidate[key] != value
        for key, value in expected.items()
    ):
        raise ArtifactValidationError("Qwen3.8 Q5 identity or safety boundary changed")
    gates = {
        "artifact_import",
        "actual_gguf_metadata",
        "template_tokenization",
        "cpu_load",
        "standard_semantics",
        "thinking_semantics_privacy",
        "expanded_context_latency",
        "latency_resource_comparison",
        "matched_application",
        "wan_offline",
        "runtime_model_rollback",
        "permissive_license_metadata_review",
    }
    qualification = candidate["qualification"]
    if (
        not isinstance(qualification, dict)
        or set(qualification) != gates
        or any(
            type(value) is not str or value not in {"passed", "partial", "failed", "not_run"}
            for value in qualification.values()
        )
        or qualification["permissive_license_metadata_review"] != "passed"
        or type(candidate["status"]) is not str
        or candidate["status"] not in {"provisioning_unselected", "verified_candidate_unselected"}
        or (
            candidate["status"] == "verified_candidate_unselected"
            and qualification["artifact_import"] != "passed"
        )
        or (
            candidate["status"] == "provisioning_unselected"
            and qualification["artifact_import"] == "passed"
        )
    ):
        raise ArtifactValidationError("Qwen3.8 Q5 qualification state is ambiguous")


def validate_qwen38_candidate(directory: Path) -> None:
    """Pin the provision-only trial; do not make discovery a serving selection."""

    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate Qwen3.8 metadata field")
            result[key] = value
        return result

    try:
        candidate = json.loads(
            (directory / "qwen3-8-27b-q8.candidate.json").read_text("utf-8"),
            object_pairs_hook=unique,
        )
    except (OSError, ValueError) as error:
        raise ArtifactValidationError("cannot parse Qwen3.8 candidate metadata") from error
    expected = {
        "schema_version": "1.0.0",
        "model_id": "nextops-qwen3-8-27b-q8-0",
        "source_repository": "https://huggingface.co/unsloth/Qwen3.8-27B-GGUF",
        "source_revision": "4ca720788d1e01f1bff70c033e0d0028fd02e502",
        "upstream_repository": "https://huggingface.co/Qwen/Qwen3.8-27B",
        "upstream_reference_revision": "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0",
        "conversion_source_revision_verified": False,
        "quantized_by": "unsloth",
        "quantization": "Q8_0",
        "filename": "Qwen3.8-27B-Q8_0.gguf",
        "size_bytes": 29047086048,
        "sha256": "a680f44a06920e5d689774823782006aa3acc8db95750323373b24139b67e348",
        "license": "Apache-2.0",
        "runtime_commit": "b29c606e28a01b1bc8c1351026a0fa6e616bf6c4",
        "cpu_only_required": True,
        "runtime_download_allowed": False,
        "deployment_selection_allowed": False,
        "public_thinking_enabled": False,
        "private_reasoning_persisted": False,
        "max_active_requests": 1,
        "max_queued_requests": 2,
    }
    if not isinstance(candidate, dict) or set(candidate) != {*expected, "status", "qualification"}:
        raise ArtifactValidationError("Qwen3.8 metadata fields changed")
    if any(type(candidate[k]) is not type(v) or candidate[k] != v for k, v in expected.items()):
        raise ArtifactValidationError("Qwen3.8 identity or qualification safety boundary changed")
    qualification = candidate["qualification"]
    gates = {
        "artifact_import",
        "template_tokenization",
        "cpu_load",
        "standard_semantics",
        "thinking_semantics_privacy",
        "latency_resource_comparison",
        "wan_offline",
        "runtime_model_rollback",
    }
    if (
        not isinstance(qualification, dict)
        or set(qualification) != gates
        or any(
            not isinstance(value, str) or value not in {"passed", "partial", "failed", "not_run"}
            for value in qualification.values()
        )
        or not isinstance(candidate["status"], str)
        or candidate["status"] not in {"provisioning_unselected", "verified_candidate_unselected"}
        or (
            candidate["status"] == "verified_candidate_unselected"
            and qualification["artifact_import"] != "passed"
        )
        or (
            candidate["status"] == "provisioning_unselected"
            and qualification["artifact_import"] == "passed"
        )
    ):
        raise ArtifactValidationError("Qwen3.8 qualification state is ambiguous")


def validate_chat_candidates(directory: Path) -> None:
    """Research metadata cannot silently become a selectable or downloaded model."""
    try:
        chat = json.loads((directory / "expanded-chat-profile.json").read_text("utf-8"))
        research = json.loads((directory / "qwen3-5-122b-a10b-research.json").read_text("utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ArtifactValidationError("cannot parse chat candidate metadata") from error
    if not isinstance(chat, dict) or not isinstance(research, dict):
        raise ArtifactValidationError("chat candidate metadata must be an object")
    expected = {
        "status": "standard_controlled_thinking_rejected",
        "standard_enabled": True,
        "thinking_enabled": False,
        "configured_context_tokens": 16384,
        "max_context_turns": 6,
        "max_context_characters": 12000,
        "standard_total_output_tokens": 1024,
        "thinking_total_output_tokens": 2048,
        "runtime_reasoning_budget_tokens": 384,
        "request_reasoning_budget_tokens": 128,
        "max_active_requests": 1,
        "max_queued_requests": 2,
        "max_conversations_per_identity": 50,
        "max_turns_per_conversation": 100,
        "max_content_bytes_per_conversation": 1048576,
        "available_retention_days": 30,
        "private_reasoning_persisted": False,
        "cpu_only": True,
        "runtime_network_downloads": False,
    }
    if any(type(chat.get(k)) is not type(v) or chat.get(k) != v for k, v in expected.items()):
        raise ArtifactValidationError("expanded chat profile changed its safety bounds or gates")
    qualification = chat.get("qualification")
    if (
        not isinstance(qualification, dict)
        or qualification.get("thinking_semantics") != "failed"
        or qualification.get("expanded_context_latency") != "failed"
    ):
        raise ArtifactValidationError("failed thinking or full-context review was concealed")
    if (
        research.get("source_revision") != "fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf"
        or research.get("total_size_bytes") != 77616511296
        or research.get("status") != "research_candidate_not_downloaded_not_selectable"
        or research.get("download_verified") is not False
        or research.get("deployment_selection_allowed") is not False
        or research.get("conversion_source_revision_verified") is not False
    ):
        raise ArtifactValidationError("122B research is not qualified for selection")
    shards = research.get("shards")
    expected_hashes = (
        "e6f74fc4e5ff7da7888cb0a135f9fafbf1265b748f5db9f72c7794061a333843",
        "1c07a0f86507ad661830a2c317f9c4450e40a836bf9133225926054ab0722316",
    )
    if (
        not isinstance(shards, list)
        or len(shards) != 2
        or any(not isinstance(s, dict) for s in shards)
        or tuple(s.get("sha256") for s in shards) != expected_hashes
        or [s.get("size_bytes") for s in shards] != [39925205312, 37691305984]
        or len({s.get("filename") for s in shards}) != 2
    ):
        raise ArtifactValidationError("122B research shard identity mismatch")


def main() -> int:
    repository_root = Path(__file__).resolve().parents[1]
    try:
        document = validate_repository(repository_root)
    except ArtifactValidationError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    flash = json.loads(
        (repository_root / "deploy/inference/qwen3-8-flash-next-q8.candidate.json").read_text(
            "utf-8"
        )
    )
    q5 = json.loads(
        (repository_root / "deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json").read_text(
            "utf-8"
        )
    )
    qwen38_q5 = json.loads(
        (repository_root / "deploy/inference/qwen3-8-27b-ud-q5-k-m.candidate.json").read_text(
            "utf-8"
        )
    )
    print(
        "PASS: inference candidate metadata is schema-valid; "
        f"status={document['status']}; runtime_binary_built="
        f"{document['evidence']['runtime_binary_built']}; "
        f"model_imported={document['evidence']['model_imported']}; "
        f"controlled_service_installed="
        f"{document['evidence']['controlled_service_installed']}; "
        f"bilingual_quality_review_passed="
        f"{document['evidence']['bilingual_quality_review_passed']}; "
        f"benchmark_run={document['evidence']['benchmark_run']}; "
        f"flash_status={flash['status']}; "
        f"flash_complete_import={flash['qualification']['artifact_import']}; "
        f"flash_selection_allowed={flash['deployment_selection_allowed']}; "
        f"q5_122b_status={q5['status']}; "
        f"q5_122b_complete_import={q5['qualification']['artifact_import']}; "
        f"q5_122b_selection_allowed={q5['deployment_selection_allowed']}; "
        f"qwen38_q5_status={qwen38_q5['status']}; "
        f"qwen38_q5_complete_import={qwen38_q5['qualification']['artifact_import']}; "
        f"qwen38_q5_selection_allowed={qwen38_q5['deployment_selection_allowed']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
