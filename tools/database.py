import os

import psycopg


def _database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL must be set to use party tools.")
    return database_url


def _normalize_input(value: str, field_name: str) -> str:
    normalized_value = value.strip().lower()
    if not normalized_value:
        raise ValueError(f"{field_name} must not be empty.")
    return normalized_value


def get_menu_suggestion(occasion: str) -> str | None:
    normalized_occasion = _normalize_input(occasion, "occasion")

    with psycopg.connect(_database_url()) as connection:
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

    return result[0] if result else None


def get_catering_service(query: str) -> str | None:
    normalized_query = query.strip().lower()

    with psycopg.connect(_database_url()) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT service_name
                FROM catering_services
                WHERE (%s = '' OR service_name ILIKE %s)
                ORDER BY rating DESC
                """,
                (normalized_query, f"%{normalized_query}%"),
            )
            result = cursor.fetchone()

    return result[0] if result else None


def get_superhero_theme(category: str) -> str | None:
    normalized_category = _normalize_input(category, "category")

    with psycopg.connect(_database_url()) as connection:
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

    return result[0] if result else None
