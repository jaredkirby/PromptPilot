"""OpenAI client module using the Responses API."""

from openai import OpenAI

from .prompts import (
    FEW_SHOT_EXAMPLE_ASSISTANT,
    FEW_SHOT_EXAMPLE_USER,
    SYSTEM_PROMPT,
)

DEFAULT_MODEL = "gpt-5-mini"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 400


def create_client(api_key: str) -> OpenAI:
    """Create an OpenAI client with the given API key."""
    return OpenAI(api_key=api_key)


def refine_prompt(
    client: OpenAI,
    user_input: str,
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> str:
    """
    Refine a user's prompt using OpenAI's Responses API.

    Args:
        client: OpenAI client instance
        user_input: The user's original prompt to refine
        model: The model to use (default: gpt-5-mini)
        temperature: Sampling temperature (default: 0.7)
        max_tokens: Maximum tokens in response (default: 400)

    Returns:
        The refined prompt suggestion from the model
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": FEW_SHOT_EXAMPLE_USER},
            {"role": "assistant", "content": FEW_SHOT_EXAMPLE_ASSISTANT},
            {"role": "user", "content": user_input},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content
