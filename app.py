import os

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


def build_agent() -> CodeAgent:
    model = OpenAIServerModel(
        model_id=os.getenv("OLLAMA_MODEL", "qwen2:7b"),
        api_base=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
        api_key="ollama",
        max_tokens=2096,
        temperature=0.5,
    )

    with open("prompts.yaml", "r", encoding="utf-8") as stream:
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
        additional_authorized_imports=["from smolagents import tool"],
    )


def main() -> None:
    agent = build_agent()
    GradioUI(agent).launch()


if __name__ == "__main__":
    main()