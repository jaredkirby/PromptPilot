# PromptPilot: An Ode to Refined Prompts

In the realm of the written word, there exists a whimsical tool known as PromptPilot. A wondrous creation to help you, my dear user, effortlessly produce effective ChatGPT prompts using the magical powers of GPT-5 mini. Like the conductor of an orchestra, PromptPilot harmonizes your intentions and fabricates a refined and targeted prompt, suited to your peculiar needs and aspirations.

![PromptPilot](https://i.imgur.com/WAWX9t4.jpeg)

## The Marvelous Features

- A delightful interface, charmingly designed for your interactions with GPT-5 mini.
- Ingenious prompt engineering techniques, ready to enhance your prompts.
- Modern Python project structure using UV package manager.
- OpenAI Responses API integration for improved performance.

## Requirements

- Python 3.12 or higher
- [UV](https://docs.astral.sh/uv/) package manager (recommended)

## The Ritual of Installation

### Using UV (Recommended)

1. Install UV if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone this curious repository from the depths of the internet:
   ```bash
   git clone https://github.com/jaredkirby/PromptPilot.git
   cd PromptPilot
   ```

3. Install dependencies and create virtual environment:
   ```bash
   uv sync
   ```

4. Awaken the Streamlit app and summon its powers:
   ```bash
   uv run streamlit run src/promptpilot/app.py
   ```

### Using pip (Alternative)

1. Clone the repository:
   ```bash
   git clone https://github.com/jaredkirby/PromptPilot.git
   cd PromptPilot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the package:
   ```bash
   pip install -e .
   ```

4. Run the app:
   ```bash
   streamlit run src/promptpilot/app.py
   ```

## The Art of Usage

1. Confide your OpenAI API key to the sidebar, where it shall remain safe.
2. Choose your desired model type from the dropdown menu (GPT-5 mini, GPT-4o, or GPT-4o-mini).
3. Scribble your question or prompt in the text input field, like a love letter to the unknown.
4. Behold the refined prompt, revealed to you in all its splendor.

## Development

### Running Tests

```bash
uv run pytest
```

### Running Linter

```bash
uv run ruff check .
uv run ruff format .
```

## Project Structure

```
PromptPilot/
├── src/
│   └── promptpilot/
│       ├── __init__.py      # Package initialization
│       ├── app.py           # Streamlit web application
│       ├── cli.py           # CLI entry point
│       ├── client.py        # OpenAI API client
│       └── prompts.py       # System prompts and examples
├── tests/
│   ├── __init__.py
│   ├── test_client.py       # Client module tests
│   └── test_prompts.py      # Prompts module tests
├── pyproject.toml           # Project configuration
└── README.md
```

## The Enchanted Dependencies

- [OpenAI](https://pypi.org/project/openai/) - For GPT-5 mini integration
- [Streamlit](https://pypi.org/project/streamlit/) - For the beautiful web interface

## Credits: A Standing Ovation

- The mind of [@Kirby_](https://twitter.com/Kirby_) and the mystic force of GPT-5 mini, intertwined in the dance of creation.
- A tip of the hat to the dapper **Jared Kirby** :wave:
  - [Twitter](https://twitter.com/Kirby_)
  - [GitHub](https://github.com/jaredkirby)
  - [LinkedIn](https://www.linkedin.com/in/jared-kirby/)
  - [Portfolio](https://www.jaredkirby.me/)

## License: The Sacred Parchment

This project is protected under the mighty MIT License - delve into the [LICENSE](LICENSE) document for the enchanting details.
