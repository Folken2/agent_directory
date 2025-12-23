"""
Configuration settings for the web search agent.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# EXA AI settings
EXA_API_KEY = os.environ.get("EXA_API_KEY")

# Search settings
DEFAULT_SEARCH_RESULTS_LIMIT = 5