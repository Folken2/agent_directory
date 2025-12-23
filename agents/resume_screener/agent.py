"""
Resume Screener Agent - Coordinates CV parsing and job requirements matching
"""

## adk imports
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import AgentTool

## config imports
from .config.llm import FAST_MODEL, REASONING_MODEL

## prompt imports
from .prompt.prompt import prompt_v0

## sub agents imports
from .sub_agents import doc_parser_agent, job_requirements_agent

root_agent = SequentialAgent(
    name="resume_screener_agent",
    sub_agents=[doc_parser_agent, job_requirements_agent],
)