"""
LLM configuration for the agent using Google AI Studio as provider.
"""

import os

from google.adk.models.lite_llm import LiteLlm

# Google AI Studio configuration - uses GOOGLE_API_KEY and direct Gemini model names
FAST_MODEL = LiteLlm(
    model="gemini-2.5-flash",
    app_name="adk-samples-directory",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

REASONING_MODEL = LiteLlm(
    model="gemini-2.5-pro",
    app_name="adk-samples-directory",
    api_key=os.getenv("GOOGLE_API_KEY"),
)
