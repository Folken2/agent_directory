# Google Maps Grounded Agent

An AI assistant that grounds answers using Google Maps search and always cites sources. Built with Google ADK and OpenRouter.

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
from simple_agent_maps_grounded.agent import root_agent

response = root_agent.run("Find restaurants near Times Square in New York")
print(response)
```

## Project Structure

```text
simple_agent_maps_grounded/
├── agent.py              # Main agent definition
├── config/
│   ├── llm.py           # LLM configuration
│   └── utils.py         # Utilities (date, etc.)
├── prompt/
│   └── prompt.py        # Agent instructions
├── sub_agent/
│   └── sub_agent.py     # Sub-agent definition (if applicable)
└── tools/
    └── web_search.py    # Web search tool (if applicable)
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

1. User asks a location-based question
2. Agent uses Google Maps grounding to find relevant places
3. Synthesizes answer from location data
4. Returns answer with sources (🔗)

## Features

- **Location Grounding**: Uses Google Maps to ground answers in real locations
- **Place Search**: Find businesses, landmarks, and points of interest
- **Source Citations**: Always cites sources for transparency
- **Geographic Context**: Provides location-aware responses

## Example Use Cases

- Find restaurants, cafes, or businesses near a location
- Get directions and location information
- Search for places by category and location
- Get reviews and ratings for places

## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK GitHub Repository](https://github.com/google/adk)
- [Google Maps Platform](https://developers.google.com/maps)
- [OpenRouter Models](https://openrouter.ai/models)

