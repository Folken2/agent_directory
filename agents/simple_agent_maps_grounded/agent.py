"""
Simple Agent with Web Search Capabilities
"""

## adk imports
from google.adk.agents import LlmAgent
from google.adk.tools import google_search, google_maps_grounding

## config imports
from .config.llm import FAST_MODEL, REASONING_MODEL

## prompt imports
from .prompt.prompt import prompt_v0



root_agent = LlmAgent(
    name="google_maps_search_agent",
    model=FAST_MODEL,
    description="AI assistant that grounds answers using google maps search and always cites sources",
    tools=[google_maps_grounding],
    instruction=prompt_v0,
)

