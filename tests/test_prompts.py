"""Tests for the prompts module."""

from promptpilot.prompts import (
    ABOUT_TEXT,
    EXAMPLE_QUESTIONS,
    FEW_SHOT_EXAMPLE_ASSISTANT,
    FEW_SHOT_EXAMPLE_USER,
    SYSTEM_PROMPT,
)


class TestPrompts:
    """Tests for prompt constants."""

    def test_system_prompt_not_empty(self) -> None:
        """System prompt should not be empty."""
        assert SYSTEM_PROMPT
        assert len(SYSTEM_PROMPT) > 100

    def test_system_prompt_contains_techniques(self) -> None:
        """System prompt should contain prompt engineering techniques."""
        techniques = [
            "clear instructions",
            "few-shot learning",
            "Chain of thought",
            "temperature",
        ]
        for technique in techniques:
            assert technique in SYSTEM_PROMPT

    def test_few_shot_example_user_not_empty(self) -> None:
        """Few-shot example user prompt should not be empty."""
        assert FEW_SHOT_EXAMPLE_USER
        assert "exercise" in FEW_SHOT_EXAMPLE_USER.lower()

    def test_few_shot_example_assistant_not_empty(self) -> None:
        """Few-shot example assistant response should not be empty."""
        assert FEW_SHOT_EXAMPLE_ASSISTANT
        assert len(FEW_SHOT_EXAMPLE_ASSISTANT) > 100

    def test_about_text_mentions_model(self) -> None:
        """About text should mention the model."""
        assert "GPT-5 mini" in ABOUT_TEXT

    def test_example_questions_not_empty(self) -> None:
        """Example questions should not be empty."""
        assert EXAMPLE_QUESTIONS
        assert "restaurant" in EXAMPLE_QUESTIONS.lower()
