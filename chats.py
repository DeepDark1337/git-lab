"""Чаты мессенджера."""


def title(kind, name, members):
    """Заголовок: название группы или участники личного чата."""
    return name if kind == "group" else ", ".join(members)


def count_members(members):
    """Количество участников чата."""
    return len(set(members))
