from .utils import get_current_date, current_date
from .llm import *

# Import all configuration variables from config.py
from .config import (
    EXA_API_KEY,
    DEFAULT_SEARCH_RESULTS_LIMIT,
    DEFAULT_JOB_SEARCH_LIMIT,
    DEFAULT_CANDIDATE_RELEVANCE_THRESHOLD,
    MAX_SEARCH_RESULTS,
    MAX_URLS_PER_REQUEST,
    MAX_SIMILAR_RESULTS,
    MAX_RESEARCH_TIMEOUT,
    MAX_QUERY_LENGTH,
    MAX_INCLUDE_DOMAINS,
    MAX_EXCLUDE_TEXT_PHRASES,
    MAX_SUBPAGES,
    MAX_LIVE_CRAWL_TIMEOUT,
    PROJECT_ID,
    LOCATION,
    GOOGLE_JOBS_API_KEY,
)
