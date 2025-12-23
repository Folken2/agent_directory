"""
Simple Agent with Web Search Capabilities
"""

## adk imports
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

## prompt imports
from .prompt.prompt import prompt_v0



root_agent = LlmAgent(
    name="web_search_agent",
    model="gemini-2.5-flash",
    description="AI assistant that grounds answers using web search and always cites sources",
    tools=[google_search],
    instruction=prompt_v0,
)

