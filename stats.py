"""Статистика чата."""


def total(counts):
    return sum(counts)


def average(counts):
    return sum(counts) / len(counts) if counts else 0
