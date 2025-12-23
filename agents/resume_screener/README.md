# Resume Screener Agent

A multi-agent AI system that screens resumes/CVs against job requirements. Built with Google ADK, using a SequentialAgent architecture with specialized sub-agents for document parsing and job requirements extraction.

## Overview

The Resume Screener Agent coordinates the resume screening process by:
- **Parsing CVs/Resumes**: Extracts structured candidate information from documents
- **Parsing Job Requirements**: Extracts requirements from job postings (URLs, documents, or text)
- **Matching Analysis**: Compares candidates against job requirements
- **Providing Insights**: Delivers match scores, strengths, gaps, and recommendations

## Quick Start

```bash
# 1. Install dependencies
uv sync --no-install-project

# 2. Set up API keys in .env file
OPENROUTER_API_KEY=your_key_here
EXA_API_KEY=your_key_here  # For web search capabilities
FAST_MODEL=openrouter/google/gemini-3-flash-preview  # Optional
REASONING_MODEL=openrouter/google/gemini-3-pro-preview  # Optional

# 3. Run the web interface
adk web
```

**Get API Keys:**

- [OpenRouter](https://openrouter.ai/keys) - for the LLM
- [EXA AI](https://dashboard.exa.ai/) - for web search (optional, used by job_requirements_agent)

## Usage

### Web Interface

```bash
adk web
```

Opens a browser interface to chat with your agent.

### Python

```python
from resume_screener.agent import root_agent

# Screen a candidate against job requirements
response = root_agent.run("""
Please screen this candidate against the job requirements:
- CV: [upload CV document]
- Job Requirements: https://example.com/job-posting
""")
print(response)
```

## Architecture

This agent uses a **SequentialAgent** architecture with two specialized sub-agents:

### 1. doc_parser_agent
**Specialized agent for parsing CVs/resumes**
- Extracts structured candidate information from CV/resume documents
- Outputs: name, skills, experience, education, languages, certifications, etc.
- Handles various document formats (PDF, DOCX, TXT, etc.)

### 2. job_requirements_agent
**Specialized agent for parsing job requirements**
- Extracts structured job requirements from multiple sources:
  - **URLs**: Job posting URLs (LinkedIn, company career pages, job boards)
  - **Documents**: Job requirements documents (uploaded artifacts)
  - **Text**: Plain text job requirements
- Outputs: required skills, experience level, education, languages, etc.
- Can automatically retrieve web content from URLs

## Project Structure

```text
resume_screener/
├── agent.py              # Main SequentialAgent coordinator
├── config/
│   ├── llm.py           # LLM configuration
│   ├── config.py        # Environment variables
│   └── utils.py         # Utilities (date, etc.)
├── prompt/
│   └── prompt.py        # Coordinator instructions
├── sub_agents/
│   ├── doc_parser_agent.py      # CV/resume parsing agent
│   └── job_requirements_agent.py  # Job requirements parsing agent
├── tools/
│   ├── artifact_tools.py  # Artifact save/load utilities
│   └── web_search.py      # Web search tool (for job postings)
├── metadata.json        # Agent metadata for web UI
└── README.md            # This file
```

## How It Works

### Workflow

1. **User provides inputs**:
   - CV/resume document (uploaded artifact or text)
   - Job requirements (URL, document, or text)

2. **Document Parsing** (can run in parallel):
   - `doc_parser_agent` extracts candidate information from CV
   - `job_requirements_agent` extracts requirements from job posting

3. **Analysis**:
   - Coordinator compares candidate profile against job requirements
   - Calculates match score (0-100%)
   - Identifies strengths and gaps

4. **Output**:
   - Structured match analysis
   - Recommendations (Yes/No/Maybe)
   - Next steps and interview questions

### Example Response Format

```text
### Job Requirements Summary
[Brief summary of extracted requirements]

### Candidate Profile Summary
[Brief summary of candidate]

### Match Analysis

**Overall Match**: 85%

**Strengths**:
- 5+ years Python experience matches requirement
- Master's degree in Computer Science exceeds requirement
- Strong match on required frameworks

**Gaps**:
- Missing certification in AWS (preferred, not required)
- Less experience with Docker than preferred

**Recommendation**: Yes - Strong candidate with minor gaps

**Next Steps**: 
- Verify Docker experience in interview
- Ask about AWS certification plans
- Explore leadership experience
```

## Customization

### Change LLM Model

Edit `config/llm.py`:

```python
FAST_MODEL = LiteLlm(
    model="openrouter/google/gemini-3-flash-preview",  # Change model here
    app_name="adk-samples-directory"
)

REASONING_MODEL = LiteLlm(
    model="openrouter/google/gemini-3-pro-preview",  # Change model here
    app_name="adk-samples-directory"
)
```

### Modify Prompts

Edit `prompt/prompt.py` to customize the coordinator's behavior, or edit individual sub-agent prompts:
- `sub_agents/doc_parser_agent.py` - CV parsing instructions
- `sub_agents/job_requirements_agent.py` - Job requirements parsing instructions

## Features

### Multi-Agent Coordination
- Uses `SequentialAgent` to coordinate specialized sub-agents
- Parallel execution when both inputs are available
- Clear delegation of responsibilities

### Flexible Input Handling
- **CVs**: Upload documents or provide text
- **Job Requirements**: URLs (auto-retrieved), documents, or plain text
- Handles various formats and languages

### Structured Output
- Match scores and percentages
- Clear strengths and gaps identification
- Actionable recommendations
- Interview question suggestions

### Artifact Management
- Automatically saves parsed documents as artifacts
- Can load and reference artifacts across the workflow
- Persistent storage for later access

## Use Cases

1. **Recruiters**: Quickly screen multiple candidates
2. **Hiring Managers**: Get objective candidate assessments
3. **HR Teams**: Standardize screening processes
4. **Job Boards**: Automated candidate matching

## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK SequentialAgent](https://google.github.io/adk-docs/agents/sequential-agent/)
- [ADK GitHub Repository](https://github.com/google/adk)
- [OpenRouter Models](https://openrouter.ai/models)
- [EXA AI Docs](https://docs.exa.ai/) - for web search capabilities
