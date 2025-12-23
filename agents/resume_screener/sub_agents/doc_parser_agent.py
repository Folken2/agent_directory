"""
CV/Resume Parser Agent - Extracts structured data from CV documents
"""

from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field, field_validator, model_validator

from google.adk.agents import LlmAgent
from google.adk.tools import load_artifacts

from ..config.llm import FAST_MODEL
from ..tools.artifact_tools import save_artifact

class Education(BaseModel):
    degree: Optional[str] = Field(None, description="Degree or qualification name")
    institution: Optional[str] = Field(None, description="School or university name")
    field_of_study: Optional[str] = Field(None, description="Field of study or major")
    graduation_year: Optional[int] = Field(None, description="Year of graduation")
    gpa: Optional[str] = Field(None, description="GPA or grade if mentioned")


class WorkExperience(BaseModel):
    job_title: Optional[str] = Field(None, description="Job title or position (also accepts 'title' field)")
    title: Optional[str] = Field(None, description="Alternative field name for job title")
    company: Optional[str] = Field(None, description="Company or organization name")
    start_date: Optional[str] = Field(None, description="Start date (month/year or year)")
    end_date: Optional[str] = Field(None, description="End date (month/year or year, or 'Present' if current)")
    description: Optional[Union[str, List[str]]] = Field(None, description="Job description or key responsibilities (can be string or list)")
    
    @model_validator(mode='after')
    def normalize_fields(self):
        """Normalize job_title from title field and description from list"""
        if not self.job_title and self.title:
            self.job_title = self.title
        if isinstance(self.description, list):
            self.description = " ".join(self.description) if self.description else None
        return self


# Simple and flexible schema for ADK output_schema
# Following ADK best practices: use simple types, List[dict] for nested structures
class CandidateInfoFlat(BaseModel):
    """Simple, flexible schema that accepts various input formats.
    
    Uses List[dict] for nested structures (work_experience, education) as per ADK best practices.
    Accepts flexible input types (str, list, dict) for skills/languages/certifications
    and normalizes them to List[str] via validators.
    """
    name: Optional[str] = Field(None, description="Full name of the candidate")
    email: Optional[str] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    location: Optional[str] = Field(None, description="City and country")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")
    summary: Optional[str] = Field(None, description="Professional summary or objective")
    # Accept flexible input types, validators will normalize to List[str]
    skills: Union[str, List[str], dict, None] = Field(default_factory=list, description="Skills - accepts string, list, or dict")
    work_experience: List[dict] = Field(default_factory=list, description="Work experience as list of dicts with keys: job_title, company, start_date, end_date, description")
    education: List[dict] = Field(default_factory=list, description="Education as list of dicts with keys: degree, institution, field_of_study, graduation_year, gpa")
    # Accept flexible input types, validators will normalize to List[str]
    languages: Union[str, List[str], None] = Field(default_factory=list, description="Languages - accepts string or list")
    certifications: Union[str, List[str], None] = Field(default_factory=list, description="Certifications - accepts string or list")
    
    @model_validator(mode='before')
    def normalize_inputs(cls, data):
        """Convert various input formats to expected types"""
        if not isinstance(data, dict):
            return data
        
        # Convert comma-separated string to list for skills
        if 'skills' in data:
            skills = data['skills']
            if isinstance(skills, str):
                data['skills'] = [s.strip() for s in skills.split(',') if s.strip()]
            elif isinstance(skills, dict):
                # Extract from dict format
                all_skills = []
                if "technical" in skills:
                    tech = skills["technical"]
                    if isinstance(tech, str):
                        all_skills.extend([s.strip() for s in tech.split(',') if s.strip()])
                    elif isinstance(tech, list):
                        all_skills.extend(tech)
                if "soft" in skills:
                    soft = skills["soft"]
                    if isinstance(soft, str):
                        all_skills.extend([s.strip() for s in soft.split(',') if s.strip()])
                    elif isinstance(soft, list):
                        all_skills.extend(soft)
                data['skills'] = all_skills
        
        # Convert comma-separated string to list for languages
        if 'languages' in data and isinstance(data['languages'], str):
            data['languages'] = [s.strip() for s in data['languages'].split(',') if s.strip()]
        
        # Convert comma-separated string to list for certifications
        if 'certifications' in data and isinstance(data['certifications'], str):
            data['certifications'] = [s.strip() for s in data['certifications'].split(',') if s.strip()]
        
        # Normalize location from dict to string
        if 'location' in data and isinstance(data['location'], dict):
            parts = []
            if "city" in data['location']:
                parts.append(str(data['location']["city"]))
            if "country" in data['location']:
                parts.append(str(data['location']["country"]))
            data['location'] = ", ".join(parts) if parts else None
        
        # Extract name from personal_information if needed
        if 'name' not in data or not data['name']:
            if 'personal_information' in data and isinstance(data['personal_information'], dict):
                data['name'] = data['personal_information'].get('name')
        
        # Normalize work_experience dicts
        if 'work_experience' in data and isinstance(data['work_experience'], list):
            for exp in data['work_experience']:
                if isinstance(exp, dict):
                    if "title" in exp and "job_title" not in exp:
                        exp["job_title"] = exp.pop("title")
                    if "description" in exp and isinstance(exp["description"], list):
                        exp["description"] = " ".join(exp["description"]) if exp["description"] else None
        
        return data
    
    @model_validator(mode='after')
    def ensure_lists(self):
        """Ensure list fields are always lists - final safety check"""
        # Handle skills - convert any format to list
        if self.skills is None:
            self.skills = []
        elif isinstance(self.skills, str):
            self.skills = [s.strip() for s in self.skills.split(',') if s.strip()]
        elif isinstance(self.skills, dict):
            # Extract from dict format
            all_skills = []
            if "technical" in self.skills:
                tech = self.skills["technical"]
                if isinstance(tech, str):
                    all_skills.extend([s.strip() for s in tech.split(',') if s.strip()])
                elif isinstance(tech, list):
                    all_skills.extend(tech)
            if "soft" in self.skills:
                soft = self.skills["soft"]
                if isinstance(soft, str):
                    all_skills.extend([s.strip() for s in soft.split(',') if s.strip()])
                elif isinstance(soft, list):
                    all_skills.extend(soft)
            self.skills = all_skills
        elif not isinstance(self.skills, list):
            self.skills = []
        
        # Handle languages - convert string to list
        if self.languages is None:
            self.languages = []
        elif isinstance(self.languages, str):
            self.languages = [s.strip() for s in self.languages.split(',') if s.strip()]
        elif not isinstance(self.languages, list):
            self.languages = []
        
        # Handle certifications - convert string to list
        if self.certifications is None:
            self.certifications = []
        elif isinstance(self.certifications, str):
            self.certifications = [s.strip() for s in self.certifications.split(',') if s.strip()]
        elif not isinstance(self.certifications, list):
            self.certifications = []
        
        return self


# Full schema with nested models for validation (used for post-processing)
class CandidateInfo(BaseModel):
    name: Optional[str] = Field(None, description="Full name of the candidate")
    personal_information: Optional[dict] = Field(None, description="Personal information object (may contain name)")
    email: Optional[str] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    location: Optional[Union[str, dict]] = Field(None, description="City and country (can be string or dict)")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")
    summary: Optional[str] = Field(None, description="Professional summary or objective")
    skills: Optional[Union[List[str], dict]] = Field(default_factory=list, description="List of technical and soft skills (can be flat list or dict with technical/soft keys)")
    work_experience: List[WorkExperience] = Field(default_factory=list, description="Work experience history")
    education: List[Education] = Field(default_factory=list, description="Educational background")
    languages: Optional[List[str]] = Field(None, description="Languages spoken with proficiency levels")
    certifications: Optional[List[str]] = Field(None, description="Professional certifications")
    
    @model_validator(mode='after')
    def normalize_fields(self):
        """Normalize fields from various formats"""
        # Extract name from personal_information if needed
        if not self.name and self.personal_information:
            self.name = self.personal_information.get("name")
        
        # Normalize skills if it's a dict
        if isinstance(self.skills, dict):
            all_skills = []
            if "technical" in self.skills:
                all_skills.extend(self.skills["technical"])
            if "soft" in self.skills:
                all_skills.extend(self.skills["soft"])
            self.skills = all_skills if all_skills else []
        
        # Normalize location if it's a dict
        if isinstance(self.location, dict):
            parts = []
            if "city" in self.location:
                parts.append(self.location["city"])
            if "country" in self.location:
                parts.append(self.location["country"])
            self.location = ", ".join(parts) if parts else None
        
        return self


doc_parser_agent = LlmAgent(
    name="cv_parser_agent",
    model=FAST_MODEL,  # Use reasoning model for better extraction accuracy
    description="AI agent that parses CV/resume documents and extracts structured candidate information",
    tools=[save_artifact, load_artifacts],
    output_schema=CandidateInfoFlat,  # Use flattened schema for ADK compatibility
    instruction="""
You are a CV/Resume parser that extracts structured information from candidate documents.

## Available Tools:
- **load_artifacts**: Load uploaded documents/artifacts into the session for processing
- **save_artifact**: Save parsed results or processed documents as artifacts

## Your Task:
1. **Load the document**: If a CV/resume is uploaded as an artifact, use **load_artifacts** to load it first
2. **Extract information**: Extract all relevant information from the CV/resume
3. **Structure the data**: Format according to the output schema
4. **Be thorough but accurate**: Only extract information that is clearly stated
5. **Handle missing data**: Leave fields as null/empty rather than guessing

## Key Fields to Extract:
- Personal information (name, contact details, location)
- Professional summary or objective
- Work experience (with dates, companies, roles, descriptions) - return as list of dicts with keys: job_title, company, start_date, end_date, description
- Education (degrees, institutions, graduation dates) - return as list of dicts with keys: degree, institution, field_of_study, graduation_year, gpa
- Skills (technical and soft skills)
- Languages and certifications if mentioned

## Important:
- **Always use load_artifacts** if a document is uploaded before parsing
- Extract dates in their original format (don't convert)
- For current positions, use "Present" as end_date
- List skills as individual items, not comma-separated strings
- **work_experience** and **education** must be lists of dictionaries (not nested objects)
- Preserve the original wording from the CV when possible
"""
)