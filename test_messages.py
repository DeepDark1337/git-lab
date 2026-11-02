"""Тесты модуля messages."""

from messages import MAX_LENGTH, is_valid, normalize


def test_normalize_strips_spaces():
    assert normalize("  привет  ") == "привет"


def test_empty_message_is_invalid():
    assert not is_valid("   ")


def test_too_long_message_is_invalid():
    assert not is_valid("x" * (MAX_LENGTH + 1))


def test_shorten_long_text():
    from messages import shorten

    assert shorten("a" * 60, limit=10) == "a" * 9 + "…"
