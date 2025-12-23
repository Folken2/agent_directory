"""
Image Agent Callbacks package.
"""

from .image_saver import after_model_callback
from .model_config import before_model_callback

__all__ = [
    "after_model_callback",
    "before_model_callback",
]

