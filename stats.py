"""Статистика чата."""


def total(counts):
    return sum(counts)


def average(counts):
    return sum(counts) / len(counts) if counts else 0


def ugly(x):
    return x * 2


def median(counts):
    ordered = sorted(counts)
    return ordered[len(ordered) // 2] if ordered else 0
