"""Streamlit web application for PromptPilot."""

import streamlit as st

from .client import create_client, refine_prompt
from .prompts import (
    ABOUT_TEXT,
    EXAMPLE_QUESTIONS,
    FEW_SHOT_EXAMPLE_ASSISTANT,
    FEW_SHOT_EXAMPLE_USER,
    SYSTEM_PROMPT,
)

PAGE_TITLE = "PromptPilot"
PAGE_ICON = "🚀"
LAYOUT = "centered"

MODEL_OPTIONS = ["gpt-5-mini", "gpt-4o", "gpt-4o-mini"]


def setup_page() -> None:
    """Configure the Streamlit page settings."""
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)


def render_header() -> None:
    """Render the main header and image."""
    st.image("https://i.imgur.com/WAWX9t4.jpeg", width=200)
    st.title(PAGE_TITLE)
    st.subheader("Effortlessly create effective ChatGPT prompts")


def render_sidebar() -> tuple[str, str]:
    """
    Render the sidebar with API key input and model selection.

    Returns:
        Tuple of (api_key, model_type)
    """
    st.sidebar.title("About")
    st.sidebar.markdown(ABOUT_TEXT)

    api_key = st.sidebar.text_input(
        "Enter your OpenAI API Key:", value="", type="password"
    )

    model_type = st.sidebar.selectbox("Select Model Type", MODEL_OPTIONS)

    st.sidebar.markdown("---")

    st.sidebar.header("Example Questions")
    st.sidebar.markdown(EXAMPLE_QUESTIONS)

    with st.sidebar.expander("The prompt used to improve your prompts!"):
        st.write(f"""
**System message:** {SYSTEM_PROMPT}

**Example User:** "{FEW_SHOT_EXAMPLE_USER}"

**Example Assistant:** "{FEW_SHOT_EXAMPLE_ASSISTANT}"
        """)

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        ":robot_face: Application created by "
        "[@Kirby_](https://twitter.com/Kirby_) & GPT-5 mini"
    )
    st.sidebar.markdown(
        ":point_right: The code for this app is available on "
        "[GitHub](https://github.com/jaredkirby/PromptPilot)"
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("Built by **Jared Kirby** :wave:")
    st.sidebar.markdown(
        "[Twitter](https://twitter.com/Kirby_) | "
        "[GitHub](https://github.com/jaredkirby) | "
        "[LinkedIn](https://www.linkedin.com/in/jared-kirby/) | "
        "[Portfolio](https://www.jaredkirby.me)"
    )

    return api_key, model_type


def get_user_input() -> str:
    """Get user input from the text field."""
    return st.text_input(
        "Ask Anything: ",
        "Hello! Will you help me improve my prompt?",
        key="input",
    )


def process_and_display_response(
    api_key: str, model_type: str, user_input: str
) -> None:
    """Process the user input and display the refined prompt."""
    if user_input and api_key:
        try:
            client = create_client(api_key)
            output = refine_prompt(client, user_input, model=model_type)
            st.markdown(f"**Pilot:** {output}")
        except Exception as e:
            st.error(f"Error communicating with OpenAI: {e}")
    else:
        st.markdown("Please enter your OpenAI API key to continue.")


def main() -> None:
    """Main entry point for the Streamlit app."""
    setup_page()
    render_header()
    api_key, model_type = render_sidebar()
    user_input = get_user_input()
    process_and_display_response(api_key, model_type, user_input)


if __name__ == "__main__":
    main()
