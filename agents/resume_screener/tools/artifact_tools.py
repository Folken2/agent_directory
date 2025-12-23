"""
Artifact management tools for saving and loading documents.
"""

from typing import Dict, Any, Optional
from google.genai import types
from google.adk.tools import FunctionTool, load_artifacts
from google.adk.tools.tool_context import ToolContext


async def save_artifact_tool(
    filename: str,
    content: str,
    mime_type: str = "text/plain",
    tool_context: Optional[ToolContext] = None,
) -> Dict[str, Any]:
    """
    Save an artifact (document or text) to the session.
    
    This tool allows you to save text content or documents as artifacts that can be
    loaded later using the load_artifacts tool. Artifacts persist across the session
    and can be accessed by other tools or agents.
    
    Args:
        filename: Name for the artifact file (e.g., "cv.pdf", "job_requirements.txt")
        content: Content to save (text content as string)
        mime_type: MIME type of the content (default: "text/plain", can be "application/pdf", "text/markdown", etc.)
        tool_context: Tool context (automatically provided)
    
    Returns:
        Dict with status, filename, version, and message
    """
    if not tool_context:
        return {
            "status": "error",
            "message": "Tool context not available"
        }
    
    try:
        # Create a Part from text content
        if mime_type == "text/plain":
            artifact_part = types.Part.from_text(text=content)
        else:
            # For other MIME types, use inline_data
            artifact_part = types.Part(
                inline_data=types.Blob(
                    mime_type=mime_type,
                    data=content.encode('utf-8') if isinstance(content, str) else content
                )
            )
        
        # Save the artifact using tool_context
        version = await tool_context.save_artifact(
            filename=filename,
            artifact=artifact_part
        )
        
        return {
            "status": "success",
            "filename": filename,
            "version": version,
            "message": f"Artifact '{filename}' saved successfully (version {version})"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to save artifact: {str(e)}"
        }


# Create FunctionTool instance - FunctionTool handles async functions
save_artifact = FunctionTool(save_artifact_tool)

# load_artifacts is already available from google.adk.tools
load_artifact = load_artifacts

