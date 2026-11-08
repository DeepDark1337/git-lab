"""Фильтр запрещённых слов."""

BANNED = {"спам"}


def is_clean(text):
    return not any(word in text.casefold() for word in BANNED)
