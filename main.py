"""Точка входа: проверка сообщения из командной строки."""

import sys

from messages import is_valid, normalize

GREETING = "Мини-мессенджер: проверка сообщений"


def main(args):
    print(GREETING)
    text = " ".join(args) or "Привет!"
    status = "ок" if is_valid(text) else "ошибка"
    print(f"{normalize(text)!r}: {status}")


if __name__ == "__main__":
    main(sys.argv[1:])
