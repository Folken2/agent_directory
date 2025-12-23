"""
Utility functions for the agent configuration.
"""

from datetime import datetime
# No need to import str as it's a built-in type


def get_current_date() -> str:
    """
    Get the current date in YYYY-MM-DD format.
    
    Returns:
        str: Current date formatted as YYYY-MM-DD
    """
    return datetime.now().strftime("%Y-%m-%d")


def current_date() -> str:
    """
    Get the current date in YYYY-MM-DD format.
    Alias for get_current_date() for backward compatibility.
    
    Returns:
        str: Current date formatted as YYYY-MM-DD
    """
    return get_current_date()


def get_current_datetime() -> str:
    """
    Get the current date and time in ISO format.
    
    Returns:
        str: Current datetime formatted as ISO string
    """
    return datetime.now().isoformat()


def get_current_timestamp() -> int:
    """
    Get the current timestamp in seconds since epoch.
    
    Returns:
        int: Current timestamp
    """
    return int(datetime.now().timestamp())
