"""
Simple Agent with Web Search Capabilities Tools package for web search.
"""

# Core intelligence tools
from .web_search import web_search
from .web_search_async import web_search_async


__all__ = [
    # Core intelligence tools
    "web_search",
    "web_search_async",
]
