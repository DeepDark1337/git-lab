"""Пользователи мессенджера."""


def display(username, display_name=""):
    """Как показать пользователя в интерфейсе."""
    return f"{display_name} (@{username})" if display_name else f"@{username}"

ROLES = ("user", "admin")

DEFAULT_ROLE = "user"

MAX_USERNAME = 32
