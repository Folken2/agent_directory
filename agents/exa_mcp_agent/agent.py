"""
Simple Agent with Exa MCP Capabilities
"""

## config imports
from .config.llm import FAST_MODEL
from .config.utils import (
    make_instruction_with_tools,
    before_agent_callback_update_tools,
)

## prompt imports
from .prompt.prompt import prompt_v0

import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

EXA_API_KEY = os.getenv("EXA_API_KEY")

# Create agent with base instruction
# Use before_agent_callback to dynamically add tools at runtime when MCP is initialized
root_agent = Agent(
    model=FAST_MODEL,
    name="exa_mcp_agent",
    instruction=prompt_v0,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url="https://mcp.exa.ai/mcp?exaApiKey=" + EXA_API_KEY,
            ),
        )
    ],
    before_agent_callback=before_agent_callback_update_tools,
)

# Try to add tools synchronously during initialization (may fail if MCP not ready)
# The callback will handle it at runtime if this fails
try:
    root_agent.instruction = make_instruction_with_tools(root_agent)
except Exception as e:
    import logging
    logger = logging.getLogger(__name__)
    logger.warning(f"Could not extract tools during initialization: {e}")
    logger.info("Tools will be added at runtime via callback")

