"""Работа с текстом сообщений мессенджера."""

MAX_LENGTH = 4000


def normalize(text):
    """Убрать пробелы по краям сообщения."""
    return text.strip()


def is_valid(text):
    """Сообщение не пустое и не длиннее MAX_LENGTH символов."""
    text = normalize(text)
    return 0 < len(text) <= MAX_LENGTH


def shorten(text, limit=50):
    """Сократить сообщение для превью в списке чатов."""
    text = normalize(text)
    return text if len(text) <= limit else text[: limit - 1] + "…"
