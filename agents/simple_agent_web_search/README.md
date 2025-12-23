# Simple Web Search Agent

A simple AI assistant that grounds answers with web search and always cites sources. Built with Google ADK and OpenRouter.

## Quick Start

```bash
# 1. Install dependencies
uv sync --no-install-project

# 2. Set up API keys in .env file
OPENROUTER_API_KEY=your_key_here
FAST_MODEL=openrouter/google/gemini-3-flash-preview  # Optional
REASONING_MODEL=openrouter/google/gemini-3-pro-preview  # Optional

# 3. Run the web interface
adk web
```

**Get API Keys:**

- [OpenRouter](https://openrouter.ai/keys) - for the LLM

## Usage

### Web Interface

```bash
adk web
```

Opens a browser interface to chat with your agent.

### Python

```python
from simple_agent_web_search.agent import root_agent

response = root_agent.run("What are the latest AI developments?")
print(response)
```

## Project Structure

```text
simple_agent_web_search/
├── agent.py              # Main agent definition
├── config/
│   ├── llm.py           # LLM configuration
│   ├── config.py        # Environment variables
│   └── utils.py         # Utilities (date, etc.)
├── prompt/
│   └── prompt.py        # Agent instructions
├── sub_agent/
│   └── sub_agent.py     # Sub-agent definition (if applicable)
└── tools/
    └── web_search.py    # Web search tool
```

## Customization

### Change LLM Model

Edit `config/llm.py`:

```python
FAST_MODEL = LiteLlm(
    model="openrouter/google/gemini-3-flash-preview",  # Change model here
    app_name="adk-samples-directory"
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
2. Agent searches web using Google Search
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

## Features

- **Web Search**: Uses Google Search to find current information
- **Source Citations**: Always cites sources for transparency
- **Real-time Information**: Accesses up-to-date web content
- **Simple Architecture**: Straightforward single-agent design

## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK GitHub Repository](https://github.com/google/adk)
- [OpenRouter Models](https://openrouter.ai/models)

