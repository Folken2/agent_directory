"""
Universal web search tool using EXA AI for comprehensive intelligence gathering.
"""

import logging
from typing import Dict, Any, Optional
import argparse
import json

from google.adk.tools.tool_context import ToolContext
from exa_py import Exa

from ..config import (
    EXA_API_KEY,
    DEFAULT_SEARCH_RESULTS_LIMIT,
)

logger = logging.getLogger(__name__)


def web_search(
    query: str,
    limit: int = DEFAULT_SEARCH_RESULTS_LIMIT,
    tool_context: Optional[ToolContext] = None,
) -> Dict[str, Any]:
    """
    Web search using EXA AI.

    Args:
        query (str): Search query
        limit (int): Maximum number of results to return (default: 5, max: 5)
        tool_context (ToolContext): Optional tool context for state

    Returns:
        Dict[str, Any]: Search results with title, url, summary, and content
    """
    try:
        if not EXA_API_KEY:
            return {
                "status": "error",
                "message": "EXA_API_KEY not configured. Please set the EXA_API_KEY environment variable or add it to your .env file.",
                "results": [],
                "total_found": 0,
            }
        
        # Validate API key format (EXA API keys are typically non-empty strings)
        if not isinstance(EXA_API_KEY, str) or len(EXA_API_KEY.strip()) == 0:
            return {
                "status": "error",
                "message": "EXA_API_KEY is empty or invalid. Please check your environment variable configuration.",
                "results": [],
                "total_found": 0,
            }

        # Enforce limits
        if limit > 5:
            logger.warning(f"Limit {limit} exceeds maximum of 5. Adjusted to 5.")
            limit = 5
        elif limit < 1:
            logger.warning(f"Limit {limit} is too low. Adjusted to 1.")
            limit = 1

        # Initialize EXA client
        exa = Exa(api_key=EXA_API_KEY)

        logger.info(f"Web search with query: {query} (limit: {limit})")

        # Build search parameters
        search_params = {
            "query": query,
            "num_results": limit,
            "text": True,
            "summary": True,
        }

        # Perform the search
        search_result = exa.search_and_contents(**search_params)

        # Process results
        results = []
        for result in search_result.results:
            processed_result = {
                "title": result.title,
                "url": result.url,
                "published_date": result.published_date,
                "summary": result.summary if hasattr(result, 'summary') else "",
                "content_snippet": result.text[:1000] if result.text else "",  # Rich content for analysis
                "source_domain": result.url,
                "relevance_score": result.score if hasattr(result, 'score') else None,
            }
            results.append(processed_result)

        # Store search in context for follow-up queries
        if tool_context:
            tool_context.state["last_web_search"] = {
                "query": query,
                "results_count": len(results),
            }

        return {
            "status": "success",
            "message": f"Found {len(results)} web results",
            "results": results,
            "total_found": len(results),
            "search_query": query,
        }

    except Exception as e:
        error_str = str(e)
        logger.error(f"Error performing web search: {error_str}")
        
        # Provide more helpful error messages for common issues
        if "x-api-key header is invalid" in error_str or "api-key" in error_str.lower():
            error_msg = (
                "EXA API key is invalid or expired. Please:\n"
                "1. Check that your EXA_API_KEY environment variable is set correctly\n"
                "2. Verify your API key at https://dashboard.exa.ai/\n"
                "3. Ensure the API key hasn't expired or been revoked"
            )
        elif "401" in error_str or "unauthorized" in error_str.lower():
            error_msg = (
                "Authentication failed. Please verify your EXA_API_KEY is correct and active."
            )
        elif "400" in error_str:
            error_msg = f"Bad request: {error_str}. Please check your search parameters."
        else:
            error_msg = f"Error performing web search: {error_str}"
        
        return {
            "status": "error",
            "message": error_msg,
            "results": [],
            "total_found": 0,
        }


if __name__ == "__main__":
    """CLI test harness for quick validation and manual testing.

    Usage:
      python -m simple_agent_web_search_EXA.tools.web_search --query "latest AI developments" --limit 5
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    parser = argparse.ArgumentParser(description="Test web_search tool")
    parser.add_argument("--query", required=False, default="latest AI developments", help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Number of results (max 5)")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print full JSON output")
    args = parser.parse_args()

    if not EXA_API_KEY:
        print("ERROR: EXA_API_KEY is not set. Please set it in your environment or .env file.")
        raise SystemExit(1)

    result = web_search(
        query=args.query, 
        limit=args.limit,
        tool_context=None
    )

    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        status = result.get("status")
        total = result.get("total_found", 0)
        print(f"Status: {status} | Total Found: {total}")
        for i, r in enumerate(result.get("results", [])[: args.limit], start=1):
            title = r.get("title") or "(no title)"
            url = r.get("url") or ""
            print(f"{i}. {title}\n   {url}")

    # Reference: Exa Search API – https://docs.exa.ai/reference/search
