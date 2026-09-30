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
    ):
        try:
            larger_schema = json.loads((directory / schema_name).read_text("utf-8"))
            larger = json.loads((directory / candidate_name).read_text("utf-8"))
            Draft202012Validator.check_schema(larger_schema)
        except (OSError, json.JSONDecodeError) as error:
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
    return document


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
        or qualification.get("expanded_context_latency") != "not_run"
    ):
        raise ArtifactValidationError("failed thinking or unrun full-context review was concealed")
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
    print(
        "PASS: inference candidate metadata is schema-valid; "
        f"status={document['status']}; runtime_binary_built="
        f"{document['evidence']['runtime_binary_built']}; "
        f"model_imported={document['evidence']['model_imported']}; "
        f"controlled_service_installed="
        f"{document['evidence']['controlled_service_installed']}; "
        f"bilingual_quality_review_passed="
        f"{document['evidence']['bilingual_quality_review_passed']}; "
        f"benchmark_run={document['evidence']['benchmark_run']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
