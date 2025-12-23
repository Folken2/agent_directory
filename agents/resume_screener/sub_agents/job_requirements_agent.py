"""
Job Requirements Parser Agent - Extracts structured data from job postings or requirement documents
"""

from typing import List, Optional, Union
from pydantic import BaseModel, Field, model_validator

from google.adk.agents import LlmAgent
from google.adk.tools import load_artifacts, url_context

from ..config.llm import FAST_MODEL
from ..tools.artifact_tools import save_artifact

class JobRequirement(BaseModel):
    """Simple, flexible schema for job requirements that accepts various input formats.
    
    Uses flexible Union types for list fields to handle comma-separated strings
    and normalizes them to List[str] via validators.
    """
    job_title: Optional[str] = Field(None, description="Job title or position name (optional)")
    company: Optional[str] = Field(None, description="Company or organization name")
    location: Optional[str] = Field(None, description="Job location (city, country, or remote)")
    employment_type: Optional[str] = Field(None, description="Full-time, Part-time, Contract, Internship, etc.")
    salary_range: Optional[str] = Field(None, description="Salary range if mentioned")
    
    # Requirements - accept flexible input types, validators will normalize to List[str]
    required_skills: Union[str, List[str], None] = Field(default_factory=list, description="Required technical and professional skills")
    preferred_skills: Union[str, List[str], None] = Field(default_factory=list, description="Preferred or nice-to-have skills")
    required_experience: Optional[str] = Field(None, description="Required years of experience or experience level")
    required_education: Optional[str] = Field(None, description="Required education level or degree")
    education_field: Union[str, List[str], None] = Field(default_factory=list, description="Preferred fields of study if specified")
    
    # Additional requirements - accept flexible input types
    languages: Union[str, List[str], None] = Field(default_factory=list, description="Required languages and proficiency levels")
    certifications: Union[str, List[str], None] = Field(default_factory=list, description="Required certifications or licenses")
    work_authorization: Optional[str] = Field(None, description="Work authorization requirements (visa, citizenship, etc.)")
    
    # Job details
    job_description: Optional[str] = Field(None, description="Detailed job description or summary")
    responsibilities: Union[str, List[str], None] = Field(default_factory=list, description="Key responsibilities and duties")
    benefits: Union[str, List[str], None] = Field(default_factory=list, description="Benefits and perks offered")
    
    # Additional info
    application_deadline: Optional[str] = Field(None, description="Application deadline if mentioned")
    start_date: Optional[str] = Field(None, description="Expected start date if mentioned")
    remote_option: Optional[Union[bool, str]] = Field(None, description="Whether remote work is available (can be bool or string)")
    
    @model_validator(mode='before')
    def normalize_inputs(cls, data):
        """Convert various input formats to expected types"""
        if not isinstance(data, dict):
            return data
        
        # List fields that can be strings - convert comma-separated strings to lists
        list_fields = [
            'required_skills', 'preferred_skills', 'education_field',
            'languages', 'certifications', 'responsibilities', 'benefits'
        ]
        
        for field in list_fields:
            if field in data and isinstance(data[field], str):
                data[field] = [s.strip() for s in data[field].split(',') if s.strip()]
        
        # Normalize location from dict to string
        if 'location' in data and isinstance(data['location'], dict):
            parts = []
            if "city" in data['location']:
                parts.append(str(data['location']["city"]))
            if "country" in data['location']:
                parts.append(str(data['location']["country"]))
            data['location'] = ", ".join(parts) if parts else None
        
        return data
    
    @model_validator(mode='after')
    def ensure_lists(self):
        """Ensure list fields are always lists - final safety check"""
        list_fields = {
            'required_skills': self.required_skills,
            'preferred_skills': self.preferred_skills,
            'education_field': self.education_field,
            'languages': self.languages,
            'certifications': self.certifications,
            'responsibilities': self.responsibilities,
            'benefits': self.benefits,
        }
        
        for field_name, field_value in list_fields.items():
            if field_value is None:
                setattr(self, field_name, [])
            elif isinstance(field_value, str):
                setattr(self, field_name, [s.strip() for s in field_value.split(',') if s.strip()])
            elif not isinstance(field_value, list):
                setattr(self, field_name, [])
        
        # Normalize remote_option if it's a string
        if isinstance(self.remote_option, str):
            self.remote_option = self.remote_option.lower() in ("true", "yes", "1", "remote", "available")
        
        return self


job_requirements_agent = LlmAgent(
    name="job_requirements_parser",
    model=FAST_MODEL,
    description="AI agent that parses job requirements from text, documents, or web URLs and extracts structured information",
    tools=[save_artifact, load_artifacts, url_context],
    output_schema=JobRequirement,
    instruction="""
You are a Job Requirements Parser that extracts structured information from job postings, job descriptions, or requirement documents.

## Available Tools:
- **load_artifacts**: Load uploaded documents/artifacts into the session for processing
- **save_artifact**: Save parsed results or processed documents as artifacts
- **url_context**: Retrieve and parse content from web URLs (job postings, LinkedIn, company career pages, etc.)

## Your Task:
1. **Handle input**: Job requirements can come in multiple formats:
   - **URL**: If a URL is provided, the **url_context** tool will automatically retrieve the web page content
   - **Document**: If a document is uploaded, use **load_artifacts** to load it first
   - **Plain text**: Extract directly from the text input
2. **Extract information**: Extract all relevant information from the job requirements
3. **Structure the data**: Format according to the output schema
4. **Be thorough but accurate**: Only extract information that is clearly stated
5. **Handle missing data**: Leave fields as null/empty rather than guessing

## Input Types:
You may receive:
1. **URL** - Job posting URL (LinkedIn, company career page, job board, etc.) - **url_context** will automatically fetch the content
2. **Plain text** - Job requirements as text input
3. **Document** - Job posting PDF, Word doc, or other document format (use load_artifacts first)

## Key Fields to Extract:

### Basic Information:
- Job title and company name
- Location (city, country, remote options)
- Employment type (full-time, part-time, contract, etc.)
- Salary range if mentioned

### Requirements:
- **Required skills** - Must-have technical and professional skills
- **Preferred skills** - Nice-to-have skills (distinguish from required)
- **Required experience** - Years of experience or experience level
- **Required education** - Degree level required
- **Education field** - Preferred fields of study (can be multiple, as a list)

### Additional Requirements:
- Languages required with proficiency levels
- Certifications or licenses needed
- Work authorization requirements

### Job Details:
- Job description or summary
- Key responsibilities and duties (as a list)
- Benefits and perks offered
- Application deadline
- Expected start date
- Remote work availability

## Important Guidelines:
- Distinguish clearly between **required** and **preferred** skills
- Extract skills as individual items, not comma-separated strings
- For experience, extract as stated (e.g., "3-5 years", "Senior level", "Entry level")
- For education, extract degree level (e.g., "Bachelor's", "Master's", "PhD")
- List responsibilities as separate items
- If remote work is mentioned, set remote_option to True
- Preserve original wording when possible, especially for job description
- If information is ambiguous, leave fields empty rather than guessing
""",
)