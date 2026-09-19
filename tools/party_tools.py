from smolagents import tool
from smolagents.tools import Tool


@tool
def suggest_menu(occasion: str) -> str:
    """Suggest a menu based on the occasion.

    Args:
        occasion (str): The type of event or party theme. Common values are "casual", "formal", "superhero", or "custom".
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    if occasion == "formal":
        return "3-course dinner with wine and dessert."
    if occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    return "Custom menu for the butler."


@tool
def catering_service_tool(query: str) -> str:
    """Return the top-rated catering service in Gotham City.

    Args:
        query (str): A search term or event keyword used to locate the best catering option.
    """
    services = {
        "Gotham Catering Co.": 4.9,
        "Wayne Manor Catering": 4.8,
        "Gotham City Events": 4.7,
    }
    return max(services, key=services.get)


class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = """Suggest creative superhero-themed party ideas for a given theme category."""

    inputs = {
        "category": {
            "type": "string",
            "description": "The type of superhero party (for example: 'classic heroes', 'villain masquerade', 'futuristic Gotham').",
        }
    }

    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
            "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
            "futuristic gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets.",
        }
        return themes.get(
            category.lower(),
            "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.",
        )


__all__ = ["suggest_menu", "catering_service_tool", "SuperheroPartyThemeTool"]
