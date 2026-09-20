import os

import psycopg
from smolagents import tool
from smolagents.tools import Tool


@tool
def suggest_menu(occasion: str) -> str:
    """Suggest a menu for a party occasion.

    Args:
        occasion: The type of occasion, such as a birthday or wedding.
    """
    normalized_occasion = occasion.strip().lower()

    with psycopg.connect(os.environ["DATABASE_URL"]) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT menu
                FROM menu_suggestions
                WHERE occasion = %s
                """,
                (normalized_occasion,),
            )
            result = cursor.fetchone()

    if result:
        return result[0]

    return "Custom menu for the butler."


@tool
def catering_service_tool(query: str) -> str:
    """Return the top-rated catering service in Gotham City.

    Args:
        query: A search term or event keyword.
    """
    with psycopg.connect(os.environ["DATABASE_URL"]) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT service_name
                FROM catering_services
                ORDER BY rating DESC
                LIMIT 1
                """
            )
            result = cursor.fetchone()

    return result[0] if result else "No catering service found."


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

    def forward(self, category: str):
        normalized_category = category.strip().lower()

        with psycopg.connect(os.environ["DATABASE_URL"]) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT theme
                    FROM superhero_party_themes
                    WHERE category = %s
                    """,
                    (normalized_category,),
                )
                result = cursor.fetchone()

        return (
            result[0]
            if result
            else "Theme not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'."
        )


__all__ = ["suggest_menu", "catering_service_tool", "SuperheroPartyThemeTool"]
