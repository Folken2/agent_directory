"""
Configuration settings for the Talent Scouter Agent.

These settings are used by the various talent scouting tools.
Vertex AI initialization is performed in the package's __init__.py
"""

import os

from dotenv import load_dotenv

# Load environment variables (this is redundant if __init__.py is imported first,
# but included for safety when importing config directly)
load_dotenv()

# Vertex AI settings
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")

# EXA AI settings
EXA_API_KEY = os.environ.get("EXA_API_KEY")

# Search settings
DEFAULT_SEARCH_RESULTS_LIMIT = 10
DEFAULT_JOB_SEARCH_LIMIT = 20
DEFAULT_CANDIDATE_RELEVANCE_THRESHOLD = 0.7
MAX_SEARCH_RESULTS = 100
MAX_URLS_PER_REQUEST = 50
MAX_SIMILAR_RESULTS = 20
MAX_RESEARCH_TIMEOUT = 300  # 5 minutes
MAX_QUERY_LENGTH = 1000
MAX_INCLUDE_DOMAINS = 10
MAX_EXCLUDE_TEXT_PHRASES = 20
MAX_SUBPAGES = 5
MAX_LIVE_CRAWL_TIMEOUT = 60  # 1 minute

# Google Jobs API settings
GOOGLE_JOBS_API_KEY = os.environ.get("GOOGLE_JOBS_API_KEY")