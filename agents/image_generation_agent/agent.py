"""
Image Generation Agent with Artifact Support
"""

## adk imports
from google.adk.agents import LlmAgent
from google.adk.tools import load_artifacts

## config imports
from .config.llm import FAST_MODEL

## tools imports
from .tools.image_generation import generate_image

## prompt imports
from .prompt.prompt import prompt_v2


root_agent = LlmAgent(
    name="image_generation_agent",
    model=FAST_MODEL,
    description="AI assistant that generates images based on a prompt",
    instruction=prompt_v2,
    tools=[generate_image, load_artifacts],
)
