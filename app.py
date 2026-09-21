import os
from pathlib import Path

import yaml
from smolagents import CodeAgent, OpenAIServerModel

from Gradio_UI import GradioUI
from tools import (
    DuckDuckGoSearchTool,
    FinalAnswerTool,
    SuperheroPartyThemeTool,
    catering_service_tool,
    suggest_menu,
)


def _configure_telemetry():
    """Initialize Langfuse tracing for smolagents."""
    from langfuse import get_client
    from openinference.instrumentation.smolagents import SmolagentsInstrumentor

    langfuse = get_client()
    SmolagentsInstrumentor().instrument()
    return langfuse


def build_agent() -> CodeAgent:
    model = OpenAIServerModel(
        model_id=os.getenv("OLLAMA_MODEL", "qwen2:7b"),
        api_base=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
        api_key="ollama",
        max_tokens=2096,
        temperature=0.5,
    )

    prompt_path = Path(__file__).resolve().parent / "prompts.yaml"
    with prompt_path.open("r", encoding="utf-8") as stream:
        prompt_templates = yaml.safe_load(stream)

    return CodeAgent(
        model=model,
        tools=[
            FinalAnswerTool(),
            DuckDuckGoSearchTool(),
            suggest_menu,
            catering_service_tool,
            SuperheroPartyThemeTool(),
        ],
        max_steps=6,
        verbosity_level=1,
        planning_interval=None,
        name=None,
        description=None,
        prompt_templates=prompt_templates,
        additional_authorized_imports=["smolagents"],
    )


def main() -> None:
    langfuse = _configure_telemetry()
    agent = build_agent()
    try:
        GradioUI(agent).launch()
    finally:
        if langfuse is not None:
            langfuse.flush()


if __name__ == "__main__":
    main()