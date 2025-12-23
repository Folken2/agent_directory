"""
Utility functions for handling image generation and artifact saving.
"""

import logging
from typing import Optional, List, Dict, Any, Tuple
import google.genai.types as types
from google.adk.agents.callback_context import CallbackContext

logger = logging.getLogger(__name__)


async def extract_and_save_images(
    response: types.GenerateContentResponse,
    context: Optional[CallbackContext] = None,
    filename_prefix: str = "generated_image",
) -> List[Dict[str, Any]]:
    """
    Extract images from agent response and save them as artifacts.
    
    Args:
        response: The GenerateContentResponse from the agent
        context: Optional CallbackContext for saving artifacts
        filename_prefix: Prefix for generated filenames
    
    Returns:
        List of dicts with image info: [{"filename": str, "version": int, "mime_type": str}, ...]
    """
    saved_images = []
    
    if not response.content or not response.content.parts:
        return saved_images
    
    image_count = 0
    for part in response.content.parts:
        # Check if this part contains image data
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            image_count += 1
            image_bytes = part.inline_data.data
            mime_type = part.inline_data.mime_type
            
            # Determine file extension from MIME type
            ext_map = {
                "image/png": "png",
                "image/jpeg": "jpg",
                "image/jpg": "jpg",
                "image/webp": "webp",
                "image/gif": "gif",
            }
            ext = ext_map.get(mime_type, "png")
            
            # Generate filename
            filename = f"{filename_prefix}_{image_count}.{ext}"
            
            # Save if context is provided
            if context:
                try:
                    # Create artifact part
                    artifact_part = types.Part.from_bytes(
                        data=image_bytes,
                        mime_type=mime_type
                    )
                    
                    # Save the artifact
                    version = await context.save_artifact(
                        filename=filename,
                        artifact=artifact_part
                    )
                    
                    saved_images.append({
                        "filename": filename,
                        "version": version,
                        "mime_type": mime_type,
                        "size_bytes": len(image_bytes),
                    })
                    
                    logger.info(
                        f"Saved generated image as artifact: {filename} (version {version})"
                    )
                except Exception as e:
                    logger.error(f"Error saving image {filename}: {str(e)}", exc_info=True)
            else:
                # Just track the image without saving
                saved_images.append({
                    "filename": filename,
                    "version": None,
                    "mime_type": mime_type,
                    "size_bytes": len(image_bytes),
                })
    
    return saved_images


async def run_agent_and_save_images(
    agent,
    prompt: str,
    context: Optional[CallbackContext] = None,
    filename_prefix: str = "generated_image",
) -> Tuple[types.GenerateContentResponse, List[Dict[str, Any]]]:
    """
    Run the agent and automatically save any generated images.
    
    Args:
        agent: The LlmAgent instance
        prompt: The prompt to send to the agent
        context: Optional CallbackContext for saving artifacts
        filename_prefix: Prefix for generated filenames
    
    Returns:
        Tuple of (response, saved_images_list)
    """
    # Run the agent
    response = await agent.run_async(prompt)
    
    # Extract and save images
    saved_images = await extract_and_save_images(
        response=response,
        context=context,
        filename_prefix=filename_prefix,
    )
    
    return response, saved_images

