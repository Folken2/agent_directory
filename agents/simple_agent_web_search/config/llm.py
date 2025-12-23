import os

from google.adk.models.lite_llm import LiteLlm


def _get_gemini_model(env_var: str, default: str) -> str:
    """Convert openrouter/google/model format to direct Gemini model name."""
    model = os.getenv(env_var, default)
    # If env var uses openrouter format, extract just the model name
    if model.startswith("openrouter/google/"):
        return model.replace("openrouter/google/", "")
    # If it already has gemini/ prefix, remove it
    if model.startswith("gemini/"):
        return model.replace("gemini/", "")
    return model


FAST_MODEL = LiteLlm(
    model=_get_gemini_model("FAST_MODEL", "gemini-3-flash-preview"),
    app_name="adk-samples-directory",
    api_key=os.getenv("GEMINI_API_KEY"),
)

REASONING_MODEL = LiteLlm(
    model=_get_gemini_model("REASONING_MODEL", "gemini-3-pro-preview"),
    app_name="adk-samples-directory",
    api_key=os.getenv("GEMINI_API_KEY"),
)
