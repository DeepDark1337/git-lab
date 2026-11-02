"""Поиск по сообщениям."""


def contains(text, query):
    return query.casefold() in text.casefold()
