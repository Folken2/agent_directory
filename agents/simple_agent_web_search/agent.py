"""
Simple Agent with Web Search Capabilities
"""

## adk imports
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

## config imports
from .config.llm import FAST_MODEL, REASONING_MODEL

## prompt imports
from .prompt.prompt import prompt_v0



root_agent = LlmAgent(
    name="web_search_agent",
    model=FAST_MODEL,
    description="AI assistant that grounds answers using web search and always cites sources",
    tools=[google_search],
    instruction=prompt_v0,
)

