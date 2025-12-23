# Agent Metadata System

This project uses a metadata system to automatically populate agent information in the web UI. Each agent directory should contain a `metadata.json` file that describes the agent.

## How It Works

1. When you create a new agent, add a `metadata.json` file in the agent's directory
2. The Next.js API route (`adk-web-ui/app/api/agents/route.ts`) automatically reads these files
3. The metadata is used to populate the agent cards and modals in the landing page

## Metadata File Format

Create a `metadata.json` file in your agent directory with the following structure:

```json
{
  "name": "your_agent_name",
  "displayName": "Your Agent Name",
  "description": "A brief description of what your agent does",
  "tools": ["tool1", "tool2", "tool3"],
  "tags": ["tag1", "tag2"],
  "useCases": ["Use case 1", "Use case 2"],
  "samplePrompts": ["Example prompt 1", "Example prompt 2"],
  "author": "Your Name",
  "githubUrl": "https://github.com/yourusername/your-repo",
  "documentation": "https://your-docs-url.com",
  "version": "1.0.0",
  "lastUpdated": "2024-01-01"
}
```

### Fields

- **name** (required): Backend/slug name used by ADK; should match the directory name (no spaces)
- **displayName** (optional): Friendly label shown in the UI (spaces and casing are fine)
- **description** (required): A human-readable description of what the agent does
- **tools** (required): An array of tool names that the agent uses
- **tags** (optional): An array of tags for categorizing the agent
- **useCases** (optional): An array of use cases that describe when to use this agent
- **samplePrompts** (optional): An array of example prompts users can try
- **author** (optional): Name of the agent creator
- **githubUrl** (optional): Link to the agent's GitHub repository
- **documentation** (optional): Link to additional documentation
- **version** (optional): Agent version number
- **lastUpdated** (optional): Last update date (ISO format)

## Example

For an agent in `my_agent/` directory:

```json
{
  "name": "my_agent",
  "displayName": "My Agent",
  "description": "AI assistant that helps with data analysis",
  "tools": ["data_loader", "statistical_analyzer", "visualization"]
}
```

## Fallback Behavior

If a `metadata.json` file doesn't exist for an agent, the system will:
1. First try to find metadata in the hardcoded fallback list
2. If not found, return basic agent info with just the name

## Adding a New Agent

1. Create your agent directory (e.g., `my_new_agent/`)
2. Create `metadata.json` in that directory with the required fields
3. The web UI will automatically pick it up when the backend lists it

## Location

The metadata files should be placed at:
```
{project_root}/
  ├── agent_name/
  │   ├── metadata.json  ← Place it here
  │   ├── agent.py
  │   └── ...
```

