# Image Generation Agent

An AI assistant that generates images based on prompts and saves them as artifacts. Built with Google ADK and OpenRouter.

## Quick Start

```bash
# 1. Install dependencies
uv sync --no-install-project

# 2. Set up API keys in .env file
OPENROUTER_API_KEY=your_key_here
FAST_MODEL=openrouter/google/gemini-3-flash-preview  # Optional
IMAGE_MODEL=openrouter/google/gemini-2.5-flash-image-preview  # Optional

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
from image_generation_agent.agent import root_agent

# Basic usage
response = root_agent.run("A futuristic cityscape at sunset")
print(response)

# Images are automatically saved as artifacts via after_model callback
response = await root_agent.run_async("A futuristic cityscape at sunset")
# Images are automatically saved - no additional code needed!
```

## Project Structure

```text
image_generation_agent/
├── agent.py              # Main agent definition
├── config/
│   ├── llm.py           # LLM configuration
│   ├── config.py        # Environment variables
│   └── utils.py         # Utilities (date, etc.)
├── prompt/
│   └── prompt.py        # Agent instructions
├── callbacks/
│   ├── image_saver.py    # after_model callback for automatic image saving
│   └── model_config.py  # Model configuration utilities
├── tools/
│   └── image_generation.py  # Image generation tool
├── utils/
│   └── image_handler.py # Image handling utilities
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

1. User provides an image generation prompt
2. Agent generates image using Gemini image model
3. Images are automatically saved as artifacts via `after_model` callback
4. Artifacts can be accessed later in the session

## Image Artifacts

Generated images are automatically saved as artifacts using Google ADK's `after_model` callback. The callback:

- **Automatically extracts** images from model responses
- **Saves them as artifacts** with generated filenames (e.g., `generated_image_1.png`)
- **Requires no additional code** - works transparently after each image generation

The `after_model_callback` is registered with the agent and automatically processes each model response:

1. Model generates an image
2. Callback extracts image data from the response
3. Image is saved as an artifact with a unique filename
4. Artifact can be accessed later using `load_artifacts`

## Example Usage

```python
# Images are automatically saved - no additional code needed!
response = await root_agent.run_async("A cyberpunk city at night")

# Access saved artifacts later
from google.adk.tools import load_artifacts
artifact = await load_artifacts(filename="generated_image_1.png")
```

## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK Artifacts](https://google.github.io/adk-docs/artifacts/)
- [ADK GitHub Repository](https://github.com/google/adk)
- [OpenRouter Models](https://openrouter.ai/models)
- [Gemini Image Generation](https://ai.google.dev/gemini-api/docs/image-generation)
