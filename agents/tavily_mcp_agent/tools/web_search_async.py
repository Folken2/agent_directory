"""
Async web search tool using EXA AI for parallel subquery execution and maximum search coverage.

This tool is designed to be called multiple times by the agent with different subqueries,
allowing ADK to execute them in parallel for comprehensive information gathering.
"""

import logging
import asyncio
from typing import List, Dict, Any, Optional
import os
import argparse
import json

import aiohttp
from google.adk.tools.tool_context import ToolContext

from ..config import (
    EXA_API_KEY,
    DEFAULT_SEARCH_RESULTS_LIMIT,
)

logger = logging.getLogger(__name__)

# Exa API endpoint
EXA_API_BASE_URL = "https://api.exa.ai"


async def web_search_async(
    query: str,
    limit: int = DEFAULT_SEARCH_RESULTS_LIMIT,
    category: Optional[str] = None,
    include_domains: Optional[List[str]] = None,
    exclude_domains: Optional[List[str]] = None,
    exclude_text: Optional[List[str]] = None,
    start_published_date: Optional[str] = None,
    end_published_date: Optional[str] = None,
    tool_context: Optional[ToolContext] = None,
) -> Dict[str, Any]:
    """
    Async web search using EXA AI for comprehensive intelligence gathering.
    
    This function is designed to be called multiple times with different subqueries,
    allowing ADK's parallel execution to run them concurrently for maximum coverage.

    Args:
        query (str): Free-form search query (the agent crafts this creatively, max 200 chars)
        limit (int): Maximum number of results to return (max 5)
        category (str, optional): Search category - 'company', 'research paper', 'news', 'pdf', 
                                 'github', 'tweet', 'personal site', 'linkedin profile', 'financial report'
        include_domains (List[str], optional): List of domains to include in search (max 3)
        exclude_domains (List[str], optional): List of domains to exclude from search (max 3)
        exclude_text (List[str], optional): List of text phrases to exclude from results (max 5)
        start_published_date (str, optional): Only content published after this date (ISO 8601 format)
        end_published_date (str, optional): Only content published before this date (ISO 8601 format)
        tool_context (ToolContext): Optional tool context for state

    Returns:
        Dict[str, Any]: Search results and metadata
    """
    try:
        if not EXA_API_KEY:
            return {
                "status": "error",
                "message": "EXA_API_KEY not configured. Please set the EXA_API_KEY environment variable or add it to your .env file.",
                "results": [],
                "total_found": 0,
            }
        
        # Validate API key format
        if not isinstance(EXA_API_KEY, str) or len(EXA_API_KEY.strip()) == 0:
            return {
                "status": "error",
                "message": "EXA_API_KEY is empty or invalid. Please check your environment variable configuration.",
                "results": [],
                "total_found": 0,
            }

        # Enforce limits to encourage focused searches
        if limit > 5:
            logger.warning(f"Limit {limit} exceeds maximum of 5. Adjusted to 5.")
            limit = 5
        elif limit < 1:
            logger.warning(f"Limit {limit} is too low. Adjusted to 1.")
            limit = 1

        # Truncate overly long queries
        if len(query) > 200:
            logger.warning(f"Query length {len(query)} exceeds maximum of 200. Truncated.")
            query = query[:200].rstrip()

        # Limit domain lists
        if include_domains and len(include_domains) > 3:
            logger.warning(f"Include domains count {len(include_domains)} exceeds maximum of 3. Using first 3.")
            include_domains = include_domains[:3]
        
        if exclude_domains and len(exclude_domains) > 3:
            logger.warning(f"Exclude domains count {len(exclude_domains)} exceeds maximum of 3. Using first 3.")
            exclude_domains = exclude_domains[:3]

        # Limit text phrases
        if exclude_text and len(exclude_text) > 5:
            logger.warning(f"Exclude text phrases count {len(exclude_text)} exceeds maximum of 5. Using first 5.")
            exclude_text = exclude_text[:5]

        logger.info(f"Async web search with query: {query} (limit: {limit})")

        # Build search request payload
        search_payload = {
            "query": query,
            "num_results": limit,
            "text": True,
            "summary": True,
        }

        # Add optional parameters if provided
        if category:
            search_payload["category"] = category
        if include_domains:
            search_payload["include_domains"] = include_domains
        if exclude_domains:
            search_payload["exclude_domains"] = exclude_domains
        if exclude_text:
            search_payload["exclude_text"] = exclude_text
        if start_published_date:
            search_payload["start_published_date"] = start_published_date
        if end_published_date:
            search_payload["end_published_date"] = end_published_date

        # Perform async HTTP request to Exa API
        async with aiohttp.ClientSession() as session:
            headers = {
                "x-api-key": EXA_API_KEY,
                "Content-Type": "application/json",
            }
            
            async with session.post(
                f"{EXA_API_BASE_URL}/search",
                headers=headers,
                json=search_payload,
                timeout=aiohttp.ClientTimeout(total=30)
            ) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"Exa API error {response.status}: {error_text}")
                
                search_data = await response.json()

        # Process results
        results = []
        if "results" in search_data:
            for result in search_data["results"]:
                processed_result = {
                    "title": result.get("title", ""),
                    "url": result.get("url", ""),
                    "published_date": result.get("published_date"),
                    "summary": result.get("summary", ""),
                    "content_snippet": (result.get("text", "") or "")[:1000],  # Rich content for analysis
                    "source_domain": result.get("url", ""),
                    "relevance_score": result.get("score"),
                }
                results.append(processed_result)

        # Store search in context for follow-up queries
        if tool_context:
            tool_context.state["last_web_search"] = {
                "query": query,
                "category": category,
                "results_count": len(results),
            }

        return {
            "status": "success",
            "message": f"Found {len(results)} web results",
            "results": results,
            "total_found": len(results),
            "search_query": query,
            "search_category": category,
            "requested_limit": limit,
            "actual_limit": limit,
            "search_params": {k: v for k, v in search_payload.items() if k not in ["query", "text", "summary"]},
        }

    except asyncio.TimeoutError:
        error_msg = "Request timed out. The Exa API may be slow or unavailable."
        logger.error(f"Timeout error: {error_msg}")
        return {
            "status": "error",
            "message": error_msg,
            "results": [],
            "total_found": 0,
        }
    except aiohttp.ClientError as e:
        error_str = str(e)
        logger.error(f"HTTP client error performing web search: {error_str}")
        return {
            "status": "error",
            "message": f"Network error: {error_str}",
            "results": [],
            "total_found": 0,
        }
    except Exception as e:
        error_str = str(e)
        logger.error(f"Error performing async web search: {error_str}")
        
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
            error_msg = f"Error performing async web search: {error_str}"
        
        return {
            "status": "error",
            "message": error_msg,
            "results": [],
            "total_found": 0,
        }


if __name__ == "__main__":
    """CLI test harness for quick validation and manual testing.

    Usage (PowerShell):
      python -m simple_agent_web_search.tools.web_search_async --query "latest AI developments 2024" --category "news" --limit 5
      python -m simple_agent_web_search.tools.web_search_async --query "Anthropic funding round" --limit 3
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    parser = argparse.ArgumentParser(description="Test web_search_async tool")
    parser.add_argument("--query", help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Number of results")
    parser.add_argument("--category", help="Search category (news, company, linkedin profile, etc.)")
    parser.add_argument("--exclude-text", nargs="+", help="Text phrases to exclude")
    parser.add_argument("--include-domains", nargs="+", help="Domains to include")
    parser.add_argument("--exclude-domains", nargs="+", help="Domains to exclude")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print full JSON output")
    args = parser.parse_args()

    if not EXA_API_KEY:
        print("ERROR: EXA_API_KEY is not set. Please set it in your environment or .env file.")
        raise SystemExit(1)

    async def run_test():
        if args.query:
            result = await web_search_async(
                query=args.query,
                limit=args.limit,
                category=args.category,
                include_domains=args.include_domains,
                exclude_domains=args.exclude_domains,
                exclude_text=args.exclude_text,
            )
        else:
            # Default test
            result = await web_search_async(
                query="latest AI developments 2024",
                limit=args.limit,
                category=args.category,
            )

        if args.pretty:
            print(json.dumps(result, indent=2))
        else:
            status = result.get("status")
            total = result.get("total_found", 0)
            category = result.get("search_category") or "general"
            print(f"Status: {status} | Category: {category} | Total Found: {total}")
            
            for i, r in enumerate(result.get("results", [])[: args.limit], start=1):
                title = r.get("title") or "(no title)"
                url = r.get("url") or ""
                score = r.get("relevance_score")
                print(f"{i}. {title}  [score={score}]\n   {url}")

    asyncio.run(run_test())

    # Reference: Exa Search API – https://docs.exa.ai/reference/search

