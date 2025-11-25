"""Tests for the client module."""

from unittest.mock import MagicMock, patch

from promptpilot.client import (
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    create_client,
    refine_prompt,
)


class TestClientConstants:
    """Tests for client module constants."""

    def test_default_model(self) -> None:
        """Default model should be gpt-5-mini."""
        assert DEFAULT_MODEL == "gpt-5-mini"

    def test_default_temperature(self) -> None:
        """Default temperature should be 0.7."""
        assert DEFAULT_TEMPERATURE == 0.7

    def test_default_max_tokens(self) -> None:
        """Default max tokens should be 400."""
        assert DEFAULT_MAX_TOKENS == 400


class TestCreateClient:
    """Tests for create_client function."""

    @patch("promptpilot.client.OpenAI")
    def test_create_client_with_api_key(self, mock_openai: MagicMock) -> None:
        """Should create an OpenAI client with the given API key."""
        api_key = "test-api-key"
        create_client(api_key)
        mock_openai.assert_called_once_with(api_key=api_key)


class TestRefinePrompt:
    """Tests for refine_prompt function."""

    @patch("promptpilot.client.OpenAI")
    def test_refine_prompt_calls_responses_api(
        self, mock_openai_cls: MagicMock
    ) -> None:
        """Should call the OpenAI Responses API with correct parameters."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.output_text = "Refined prompt text"
        mock_client.responses.create.return_value = mock_response

        result = refine_prompt(mock_client, "Test input")

        assert result == "Refined prompt text"
        mock_client.responses.create.assert_called_once()

        call_kwargs = mock_client.responses.create.call_args.kwargs
        assert call_kwargs["model"] == DEFAULT_MODEL
        assert call_kwargs["temperature"] == DEFAULT_TEMPERATURE
        assert call_kwargs["max_output_tokens"] == DEFAULT_MAX_TOKENS

    @patch("promptpilot.client.OpenAI")
    def test_refine_prompt_with_custom_model(self, mock_openai_cls: MagicMock) -> None:
        """Should use custom model when specified."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.output_text = "Refined prompt"
        mock_client.responses.create.return_value = mock_response

        refine_prompt(mock_client, "Test input", model="gpt-4o")

        call_kwargs = mock_client.responses.create.call_args.kwargs
        assert call_kwargs["model"] == "gpt-4o"

    @patch("promptpilot.client.OpenAI")
    def test_refine_prompt_includes_user_input(
        self, mock_openai_cls: MagicMock
    ) -> None:
        """Should include user input in the request."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.output_text = "Refined prompt"
        mock_client.responses.create.return_value = mock_response

        user_input = "Help me write a better prompt"
        refine_prompt(mock_client, user_input)

        call_kwargs = mock_client.responses.create.call_args.kwargs
        messages = call_kwargs["input"]
        assert any(
            msg.get("role") == "user" and user_input in msg.get("content", "")
            for msg in messages
        )
