# Hugging Face Party Agent

A Gradio-based party-planning assistant built with `smolagents` and a local Ollama model. The agent can help plan themed events by combining web search, menu suggestions, catering service recommendations, and superhero-inspired party concepts.

## Overview

This project creates a conversational agent that answers party-planning requests using a set of custom tools backed by a PostgreSQL database and optional web search. The main entry point is `app.py`, which builds a `CodeAgent` and launches the Gradio interface from `Gradio_UI.py`.

## What the agent can do

- Suggest party menus based on occasion
- Recommend catering services by keyword
- Generate superhero-themed party ideas
- Search the web for relevant event information
- Provide a chat-based experience through Gradio

## Project structure

- `app.py` – configures the model and agent, then launches the UI
- `Gradio_UI.py` – streaming Gradio chat interface
- `prompts.yaml` – prompt templates for the agent
- `tools/` – custom tools and database access helpers
- `requirements.txt` – Python dependencies

## Requirements

- Python 3.10+
- Ollama installed locally
- A running Ollama server
- PostgreSQL database with the expected party tables

## Setup

1. Open a terminal in the project root.
2. Create and activate a virtual environment if needed:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Pull and run the model with Ollama:

```powershell
ollama pull qwen2:7b
ollama serve
```

5. Set the required environment variables before starting the app:

```powershell
$env:OLLAMA_MODEL = "qwen2:7b"
$env:OLLAMA_BASE_URL = "http://localhost:11434/v1"
$env:DATABASE_URL = "postgresql://username:password@localhost:5432/party_agent"
$env:LANGFUSE_PUBLIC_KEY = "pk-lf-..."
$env:LANGFUSE_SECRET_KEY = "sk-lf-..."
$env:LANGFUSE_HOST = "https://cloud.langfuse.com"
```

The Langfuse keys are required for traces to appear in the Langfuse dashboard. Start the app from the same PowerShell session after setting them. The app instruments smolagents at startup and flushes buffered traces when it exits.

> The application defaults to `qwen2:7b` at `http://localhost:11434/v1` if these variables are not set, but `DATABASE_URL` is required for the party tools to work.

## Database requirements

The custom tools query a PostgreSQL database through `tools/database.py`. The app expects these tables to exist:

- `menu_suggestions` with columns such as `occasion` and `menu`
- `catering_services` with columns such as `service_name` and `rating`
- `superhero_party_themes` with columns such as `category` and `theme`

The queries in the code use these tables to answer menu, catering, and theme generation requests. If the database is missing or `DATABASE_URL` is unset, the related tool calls will fail.

## Run the app

From the project root, start the Gradio server:

```powershell
python app.py
```

The app will open a local Gradio interface in the browser. You can then ask the agent to create party plans, suggest ideas, or help with event details.

## Example prompts

- "Plan a superhero-themed birthday party for 20 guests."
- "Suggest a menu for a wedding reception."
- "Find a catering service for a Gotham-themed gala."
- "Give me fun party ideas for a futuristic villain masquerade."

## Troubleshooting

### Ollama connection issues

- Make sure the Ollama server is running with `ollama serve`.
- Confirm the model is available: `ollama pull qwen2:7b`.
- Verify the endpoint matches the configured `OLLAMA_BASE_URL`.

### Database errors

- Ensure `DATABASE_URL` is set in the current shell/session.
- Check that the Postgres service is reachable.
- Verify the expected tables and columns exist.

### Dependency issues

```powershell
pip install -r requirements.txt
```

The tracing dependencies are pinned to versions compatible with the configured smolagents integration.

If needed, recreate the virtual environment and reinstall dependencies.

## Notes

This project is intentionally configured for a local-first setup, with an open-source model running via Ollama and structured party data stored in PostgreSQL. It is a good fit for experimentation and local event-planning agent workflows.
