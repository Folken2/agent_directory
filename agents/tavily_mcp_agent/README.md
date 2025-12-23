# EXA Web Search Agent

A simple AI assistant that grounds answers with web search and always cites sources. Built with Google ADK, EXA AI, and OpenRouter.

## Quick Start

```bash
# 1. Install dependencies
uv sync --no-install-project

# 2. Set up API keys in .env file
OPENROUTER_API_KEY=your_key_here
EXA_API_KEY=your_key_here

# 3. Run the web interface
adk web
```

**Get API Keys:**

- [OpenRouter](https://openrouter.ai/keys) - for the LLM
- [EXA AI](https://dashboard.exa.ai/) - for web search

## Usage

### Web Interface

```bash
adk web
```

Opens a browser interface to chat with your agent.

### Python

```python
from simple_agent_web_search_EXA.agent import root_agent

response = root_agent.run("What are the latest AI developments?")
print(response)
```

## Project Structure

```text
simple_agent_web_search_EXA/
├── agent.py              # Main agent definition
├── config/
│   ├── llm.py           # LLM configuration
│   ├── config.py        # Environment variables
│   └── utils.py         # Utilities (date, etc.)
├── prompt/
│   └── prompt.py        # Agent instructions
└── tools/
    └── web_search.py    # EXA AI search tool
```

## Customization

### Change LLM Model

Edit `config/llm.py`:

```python
FAST_MODEL = LiteLlm(
    model="openrouter/google/gemini-2.5-flash",  # Change model here
    app_name="talent_scout"
)
```

Then update `agent.py`:

```python
root_agent = LlmAgent(
    model=FAST_MODEL,  # or REASONING_MODEL
    # ...
)
```

### Modify Prompt

Edit `prompt/prompt.py` to change agent behavior:

```python
prompt_v0 = f"""
You are a helpful AI assistant...
# Your custom instructions here
"""
```

## How It Works

1. User asks a question
2. Agent searches web using EXA AI
3. Synthesizes answer from results
4. Returns answer with sources (🔗)

## Example Response

```text
[Answer based on search results]

---

## 🔗 Sources

1. [Title](URL1)
2. [Title](URL2)
```

## Resources

- [Google ADK](https://github.com/google/adk)
- [EXA AI Docs](https://docs.exa.ai/)
- [OpenRouter Models](https://openrouter.ai/models)
