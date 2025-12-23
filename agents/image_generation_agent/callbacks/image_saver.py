"""
Callback handler to automatically save generated images as artifacts.
"""

import logging
import re
import base64
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse
from google.genai.types import Part

logger = logging.getLogger(__name__)


async def after_model_callback(
    callback_context: CallbackContext,
    llm_response: LlmResponse,
) -> None:
    """
    Callback to automatically extract and save images from model responses.
    
    This callback processes the model's response after generation, extracts any image data,
    and saves it as an artifact with a generated filename.
    """
    logger.info("=" * 60)
    logger.info("after_model_callback: CALLBACK EXECUTED")
    logger.info("=" * 60)
    
    try:
        # Log response structure for debugging
        logger.info(f"llm_response type: {type(llm_response)}")
        
        # Log all non-private attributes and their values
        public_attrs = [attr for attr in dir(llm_response) if not attr.startswith('_')]
        logger.info(f"llm_response public attributes: {public_attrs}")
        
        # Try to get the full response as dict to see structure
        try:
            response_dict = llm_response.model_dump() if hasattr(llm_response, 'model_dump') else {}
            logger.info(f"llm_response as dict keys: {list(response_dict.keys()) if response_dict else 'N/A'}")
            logger.info(f"llm_response dict (first 1000 chars): {str(response_dict)[:1000]}")
            
            # Check for images field in the response (OpenRouter format)
            if isinstance(response_dict, dict):
                # Check if content has images
                if 'content' in response_dict and response_dict['content']:
                    content_dict = response_dict['content']
                    if isinstance(content_dict, dict):
                        logger.info(f"content dict keys: {list(content_dict.keys())}")
                        # Check for images in content
                        if 'images' in content_dict:
                            logger.info(f"Found 'images' field in content: {content_dict['images']}")
        except Exception as e:
            logger.info(f"Could not convert response to dict: {e}")
        
        # Check if content exists
        if not hasattr(llm_response, 'content'):
            logger.warning("llm_response has no 'content' attribute")
            return
        
        logger.info(f"llm_response.content: {llm_response.content}")
        logger.info(f"llm_response.content type: {type(llm_response.content)}")
        
        # Log all content attributes
        if llm_response.content:
            content_attrs = [attr for attr in dir(llm_response.content) if not attr.startswith('_')]
            logger.info(f"content attributes: {content_attrs}")
            try:
                content_dict = llm_response.content.model_dump() if hasattr(llm_response.content, 'model_dump') else {}
                logger.info(f"content as dict: {content_dict}")
            except Exception as e:
                logger.info(f"Could not convert content to dict: {e}")
        
        if not llm_response.content:
            logger.warning("llm_response.content is None or empty")
            return
        
        # Check if parts exist
        if not hasattr(llm_response.content, 'parts'):
            logger.warning("llm_response.content has no 'parts' attribute")
            return
        
        logger.info(f"llm_response.content.parts: {llm_response.content.parts}")
        logger.info(f"llm_response.content.parts type: {type(llm_response.content.parts)}")
        logger.info(f"Number of parts: {len(llm_response.content.parts) if llm_response.content.parts else 0}")
        
        # Check other response attributes that might contain images
        for attr_name in ['finish_reason', 'usage_metadata', 'error_message', 'error_code']:
            if hasattr(llm_response, attr_name):
                attr_value = getattr(llm_response, attr_name)
                logger.info(f"llm_response.{attr_name}: {attr_value}")
        
        if not llm_response.content.parts:
            logger.warning("=" * 60)
            logger.warning("⚠️  llm_response.content.parts is empty - image may not be in response yet")
            logger.warning("This could mean:")
            logger.warning("  1. The callback is called before image generation completes")
            logger.warning("  2. The image is returned in a different format/location")
            logger.warning("  3. The model didn't generate an image")
            logger.warning("=" * 60)
            return
        
        image_count = 0
        for idx, part in enumerate(llm_response.content.parts):
            logger.info(f"--- Processing part {idx + 1} ---")
            logger.info(f"part type: {type(part)}")
            
            # Log all part fields for debugging
            try:
                part_dict = part.model_dump() if hasattr(part, 'model_dump') else {}
                logger.info(f"part as dict keys: {list(part_dict.keys())}")
                logger.info(f"part dict values: {part_dict}")
            except Exception as e:
                logger.info(f"Could not convert part to dict: {e}")
            
            # Check inline_data first (standard image format)
            if hasattr(part, 'inline_data') and part.inline_data:
                logger.info(f"Found inline_data: mime_type={part.inline_data.mime_type}")
                if part.inline_data.mime_type and part.inline_data.mime_type.startswith("image/"):
                    image_count += 1
                    image_bytes = part.inline_data.data
                    mime_type = part.inline_data.mime_type
                    
                    logger.info(f"Found image #{image_count}: mime_type={mime_type}, size={len(image_bytes)} bytes")
                    
                    ext_map = {
                        "image/png": "png",
                        "image/jpeg": "jpg",
                        "image/jpg": "jpg",
                        "image/webp": "webp",
                        "image/gif": "gif",
                    }
                    ext = ext_map.get(mime_type, "png")
                    filename = f"generated_image_{image_count}.{ext}"
                    
                    try:
                        version = await callback_context.save_artifact(
                            filename=filename,
                            artifact=part
                        )
                        logger.info("=" * 60)
                        logger.info(f"✅ SUCCESS: Saved generated image as artifact")
                        logger.info(f"   Filename: {filename}")
                        logger.info(f"   Version: {version}")
                        logger.info(f"   MIME type: {mime_type}")
                        logger.info(f"   Size: {len(image_bytes)} bytes")
                        logger.info("=" * 60)
                    except Exception as save_error:
                        logger.error(f"❌ FAILED to save artifact {filename}: {str(save_error)}", exc_info=True)
                    continue
            
            # Check file_data (alternative image format)
            if hasattr(part, 'file_data') and part.file_data:
                logger.info(f"Found file_data: {part.file_data}")
                # file_data might contain image references
                logger.info("⚠️  file_data found but not yet handled - may contain image reference")
            
            # Check if text contains image data (base64, URL, etc.)
            if hasattr(part, 'text') and part.text:
                text_content = part.text
                logger.info(f"Part has text content (full text): {text_content}")
                
                # Check for base64 image data in text
                base64_pattern = r'data:image/([^;]+);base64,([A-Za-z0-9+/=]+)'
                base64_match = re.search(base64_pattern, text_content)
                if base64_match:
                    logger.info("Found base64 image data in text!")
                    mime_type = f"image/{base64_match.group(1)}"
                    base64_data = base64_match.group(2)
                    try:
                        image_bytes = base64.b64decode(base64_data)
                        image_count += 1
                        
                        ext_map = {
                            "png": "png",
                            "jpeg": "jpg",
                            "jpg": "jpg",
                            "webp": "webp",
                            "gif": "gif",
                        }
                        ext = ext_map.get(base64_match.group(1), "png")
                        filename = f"generated_image_{image_count}.{ext}"
                        
                        # Create a Part from bytes
                        image_part = Part.from_bytes(data=image_bytes, mime_type=mime_type)
                        
                        version = await callback_context.save_artifact(
                            filename=filename,
                            artifact=image_part
                        )
                        logger.info("=" * 60)
                        logger.info(f"✅ SUCCESS: Saved base64 image from text as artifact")
                        logger.info(f"   Filename: {filename}")
                        logger.info(f"   Version: {version}")
                        logger.info(f"   MIME type: {mime_type}")
                        logger.info(f"   Size: {len(image_bytes)} bytes")
                        logger.info("=" * 60)
                    except Exception as e:
                        logger.error(f"Failed to decode/save base64 image: {e}", exc_info=True)
                
                # Check for image URLs in text
                url_pattern = r'https?://[^\s]+\.(?:png|jpg|jpeg|gif|webp)'
                url_matches = re.findall(url_pattern, text_content, re.IGNORECASE)
                if url_matches:
                    logger.info(f"Found image URL(s) in text: {url_matches}")
                    logger.info("⚠️  Image URLs found but not downloading - may need URL handling")
        
        # If no images found in parts, check for OpenRouter format images in content
        if image_count == 0:
            logger.info("=" * 60)
            logger.info("Checking for OpenRouter image format (message.images field)...")
            logger.info("=" * 60)
            
            # Check if content has an images attribute (OpenRouter format)
            if hasattr(llm_response.content, 'images'):
                content_images = getattr(llm_response.content, 'images', None)
                logger.info(f"content.images: {content_images}")
                if content_images:
                    logger.info(f"Found images in content.images: {len(content_images)} image(s)")
                    for idx, img in enumerate(content_images):
                        try:
                            # OpenRouter format: images[].image_url.url (base64 data URL)
                            if hasattr(img, 'image_url'):
                                image_url_obj = img.image_url
                                if hasattr(image_url_obj, 'url'):
                                    image_url = image_url_obj.url
                                    logger.info(f"Image {idx + 1} URL (first 100 chars): {image_url[:100]}")
                                    
                                    # Extract base64 data from data URL
                                    if image_url.startswith('data:image/'):
                                        # Format: data:image/png;base64,<base64_data>
                                        parts = image_url.split(',', 1)
                                        if len(parts) == 2:
                                            mime_part = parts[0]  # data:image/png;base64
                                            base64_data = parts[1]
                                            
                                            # Extract MIME type
                                            mime_match = re.search(r'data:image/([^;]+)', mime_part)
                                            mime_type = f"image/{mime_match.group(1)}" if mime_match else "image/png"
                                            
                                            try:
                                                image_bytes = base64.b64decode(base64_data)
                                                image_count += 1
                                                
                                                ext_map = {
                                                    "png": "png",
                                                    "jpeg": "jpg",
                                                    "jpg": "jpg",
                                                    "webp": "webp",
                                                    "gif": "gif",
                                                }
                                                ext = ext_map.get(mime_match.group(1) if mime_match else "png", "png")
                                                filename = f"generated_image_{image_count}.{ext}"
                                                
                                                # Create a Part from bytes
                                                image_part = Part.from_bytes(data=image_bytes, mime_type=mime_type)
                                                
                                                version = await callback_context.save_artifact(
                                                    filename=filename,
                                                    artifact=image_part
                                                )
                                                logger.info("=" * 60)
                                                logger.info(f"✅ SUCCESS: Saved OpenRouter image as artifact")
                                                logger.info(f"   Filename: {filename}")
                                                logger.info(f"   Version: {version}")
                                                logger.info(f"   MIME type: {mime_type}")
                                                logger.info(f"   Size: {len(image_bytes)} bytes")
                                                logger.info("=" * 60)
                                            except Exception as e:
                                                logger.error(f"Failed to decode/save OpenRouter image: {e}", exc_info=True)
                        except Exception as e:
                            logger.error(f"Error processing OpenRouter image: {e}", exc_info=True)
            
            # Also check the raw response dict for images
            try:
                response_dict = llm_response.model_dump() if hasattr(llm_response, 'model_dump') else {}
                logger.info(f"Full response_dict structure check:")
                logger.info(f"  - Top level keys: {list(response_dict.keys())}")
                
                # Check all possible locations for images
                if isinstance(response_dict, dict):
                    # Check content.images
                    if 'content' in response_dict:
                        content_dict = response_dict.get('content', {})
                        if isinstance(content_dict, dict):
                            logger.info(f"  - content keys: {list(content_dict.keys())}")
                            if 'images' in content_dict:
                                images_list = content_dict['images']
                                logger.info(f"  ✅ Found images in response_dict.content.images: {len(images_list)} image(s)")
                                # Process images here
                            
                            # Check if parts contain images in a different format
                            if 'parts' in content_dict:
                                for part_idx, part_dict in enumerate(content_dict.get('parts', [])):
                                    if isinstance(part_dict, dict):
                                        logger.info(f"  - part {part_idx} keys: {list(part_dict.keys())}")
                                        # Check for images in part
                                        if 'images' in part_dict:
                                            logger.info(f"  ✅ Found images in part {part_idx}")
                    
                    # Check custom_metadata (might contain raw response)
                    if 'custom_metadata' in response_dict and response_dict['custom_metadata']:
                        logger.info(f"  - custom_metadata: {response_dict['custom_metadata']}")
                        if isinstance(response_dict['custom_metadata'], dict) and 'images' in response_dict['custom_metadata']:
                            logger.info(f"  ✅ Found images in custom_metadata")
                    
                    # Check if there's a hidden _raw_response or similar
                    for attr in dir(llm_response):
                        if not attr.startswith('_') or attr.startswith('__'):
                            continue
                        if 'raw' in attr.lower() or 'response' in attr.lower() or 'litellm' in attr.lower():
                            try:
                                value = getattr(llm_response, attr, None)
                                if value:
                                    logger.info(f"  - Found hidden attr {attr}: {type(value)}")
                                    if isinstance(value, dict) and 'images' in value:
                                        logger.info(f"  ✅ Found images in {attr}")
                            except:
                                pass
            except Exception as e:
                logger.info(f"Could not check response_dict for images: {e}", exc_info=True)
        
        if image_count == 0:
            logger.warning("=" * 60)
            logger.warning("⚠️  No images found in response (checked parts, content.images, and response_dict)")
            logger.warning("=" * 60)
        else:
            logger.info(f"Total images processed: {image_count}")
            
    except Exception as e:
        logger.error("=" * 60)
        logger.error(f"❌ ERROR in after_model_callback: {str(e)}")
        logger.error("=" * 60, exc_info=True)

