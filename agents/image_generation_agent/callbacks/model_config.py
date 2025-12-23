"""
Callback to configure model requests for image generation.
"""

import logging
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest

logger = logging.getLogger(__name__)


async def before_model_callback(
    callback_context: CallbackContext,
    llm_request: LlmRequest,
) -> None:
    """
    Callback to ensure OpenRouter requests include modalities parameter for image generation.
    
    This ensures that when using OpenRouter image generation models, the request
    includes modalities=["image", "text"] so images are actually generated.
    """
    try:
        # Check if this is an OpenRouter model
        if hasattr(llm_request, 'model') and 'openrouter' in str(llm_request.model).lower():
            logger.info("=" * 60)
            logger.info("before_model_callback: Configuring OpenRouter image generation")
            logger.info(f"Model: {llm_request.model}")
            
            # Try to add modalities parameter
            # Note: This might need to be done differently depending on ADK/LiteLLM API
            # Check if we can modify the request
            if hasattr(llm_request, 'extra_body'):
                if llm_request.extra_body is None:
                    llm_request.extra_body = {}
                llm_request.extra_body['modalities'] = ['image', 'text']
                logger.info("Added modalities=['image', 'text'] to extra_body")
            elif hasattr(llm_request, 'modalities'):
                llm_request.modalities = ['image', 'text']
                logger.info("Set modalities=['image', 'text']")
            else:
                logger.warning("Could not find way to set modalities parameter")
                logger.info(f"llm_request attributes: {[attr for attr in dir(llm_request) if not attr.startswith('_')]}")
            
            logger.info("=" * 60)
    except Exception as e:
        logger.error(f"Error in before_model_callback: {str(e)}", exc_info=True)

