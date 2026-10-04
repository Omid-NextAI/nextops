"""Owner-scoped durable general chat; never infrastructure evidence or authority."""

import json
from typing import Literal, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from nextops.contracts.assistant import AssistantRequest, AssistantResponse
from nextops.contracts.models import FrozenContract


class SavedContextTurn(FrozenContract):
    question: str = Field(min_length=1, max_length=4_000)
    answer: str = Field(min_length=1, max_length=16_000)


class ConversationAssistantRequest(AssistantRequest):
    """Server-built history and budget, not the public message contract."""

    max_output_tokens: int = Field(default=1_024, ge=32, le=2_048)
    history: tuple[SavedContextTurn, ...] = Field(default=(), max_length=6)
    history_omitted: bool = False
    thinking: bool = False

    @model_validator(mode="after")
    def context_bound(self) -> Self:
        if len(json.dumps([t.model_dump() for t in self.history], ensure_ascii=False)) > 12_000:
            raise ValueError("saved context exceeds 12000 characters")
        return self


class ConversationCreate(FrozenContract):
    locale: Literal["en", "fa"]


class ConversationMessageRequest(FrozenContract):
    request_id: UUID
    locale: Literal["en", "fa"]
    question: str = Field(min_length=1, max_length=4_000)
    thinking: bool = False


class ConversationSummary(FrozenContract):
    conversation_id: UUID
    title: str = Field(min_length=1, max_length=80)
    locale: Literal["en", "fa"]
    created_at: AwareDatetime
    updated_at: AwareDatetime
    expires_at: AwareDatetime
    turn_count: int = Field(ge=0, le=100)


class SavedMessage(FrozenContract):
    request_id: UUID
    sequence: int = Field(ge=1, le=100)
    question: str = Field(min_length=1, max_length=4_000)
    assistant: AssistantResponse
    thinking_requested: bool
    context_turns: int = Field(ge=0, le=6)
    context_omitted: bool
    created_at: AwareDatetime


class ConversationPage(FrozenContract):
    conversation: ConversationSummary
    messages: tuple[SavedMessage, ...] = Field(max_length=20)
    before_sequence: int | None = Field(default=None, ge=1, le=100)


class ConversationCapabilities(FrozenContract):
    enabled: bool
    thinking_enabled: bool
    context_characters: Literal[12_000] = 12_000
    context_turns: Literal[6] = 6
    retention_days: Literal[30] = 30


class ConversationAnswer(FrozenContract):
    conversation_id: UUID
    message: SavedMessage
