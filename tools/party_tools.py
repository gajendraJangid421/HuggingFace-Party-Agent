from smolagents import tool
from smolagents.tools import Tool

from .database import get_catering_service, get_menu_suggestion, get_superhero_theme

@tool
def suggest_menu(occasion: str) -> str:
    """Suggest a menu for a party occasion.

    Args:
        occasion: The type of occasion, such as a birthday or wedding.
    """
    return get_menu_suggestion(occasion) or "No menu suggestion found for that occasion."


@tool
def catering_service_tool(query: str) -> str:
    """Return the top-rated matching catering service in Gotham City.

    Args:
        query: A search term or event keyword.
    """
    return get_catering_service(query) or "No catering service found."


class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = "Suggest creative superhero-themed party ideas for a given theme category."

    inputs = {
        "category": {
            "type": "string",
            "description": "The superhero party theme category.",
        }
    }

    output_type = "string"

    def forward(self, category: str) -> str:
        theme = get_superhero_theme(category)
        return theme or "Theme not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'."


__all__ = ["suggest_menu", "catering_service_tool", "SuperheroPartyThemeTool"]
