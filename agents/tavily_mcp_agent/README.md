# Tavily MCP Agent

An AI assistant that uses Tavily's MCP (Model Context Protocol) server to search the web and extract information from websites. Built with Google ADK, Tavily MCP, and OpenRouter.

## Quick Start

```bash
# 1. Install dependencies
uv sync --no-install-project

# 2. Set up API keys in .env file
OPENROUTER_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
FAST_MODEL=openrouter/google/gemini-3-flash-preview  # Optional

# 3. Run the web interface
adk web
```

**Get API Keys:**

- [OpenRouter](https://openrouter.ai/keys) - for the LLM
- [Tavily](https://tavily.com/) - for web search and content extraction

## Usage

### Web Interface

```bash
adk web
```

Opens a browser interface to chat with your agent.

### Python

```python
from tavily_mcp_agent.agent import root_agent

response = root_agent.run("What are the latest AI developments?")
print(response)
```

## Project Structure

```text
tavily_mcp_agent/
├── agent.py              # Main agent definition with Tavily MCP integration
├── config/
│   ├── llm.py           # LLM configuration
│   └── utils.py         # MCP tool handling utilities
├── prompt/
│   └── prompt.py        # Agent instructions
├── tools/
│   ├── rag_search.py    # RAG search tool
│   └── web_search_async.py  # Web search tool
└── metadata.json        # Agent metadata for web UI
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
2. Agent uses Tavily MCP server to search the web
3. MCP tools are dynamically loaded at runtime via callback
4. Agent can search, extract content, and perform RAG searches
5. Synthesizes answer from results
6. Returns answer with sources (🔗)

## MCP Integration

This agent uses the Tavily MCP server to access web search and content extraction capabilities. The MCP connection:
- Connects to Tavily's MCP endpoint via HTTPS
- Requires `TAVILY_API_KEY` for authentication
- Dynamically loads available tools at runtime
- Provides web search, content extraction, and RAG search capabilities

## Example Response

```text
[Answer based on search results]

---

## 🔗 Sources

1. [Title](URL1)
2. [Title](URL2)
```

## Features

- **Web Search**: Search the web for current information
- **Content Extraction**: Extract and process content from web pages
- **RAG Search**: Perform retrieval-augmented generation searches
- **Source Citations**: Always cites sources for transparency

## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK GitHub Repository](https://github.com/google/adk)
- [Tavily](https://tavily.com/)
- [Tavily API Docs](https://docs.tavily.com/)
- [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)
- [OpenRouter Models](https://openrouter.ai/models)
