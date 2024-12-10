# -*- coding: utf-8 -*-
"""Функция для получения аргументов командной строки."""

from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    """Получает аргументы, переданные из командной строки."""
    global __args

    parser: ArgumentParser = ArgumentParser(
        description="Simple Emailer Exec - утилита для отправки писем"
                    " через SMTP Gmail."
    )

    parser.add_argument(
        "-r",
        help="Адрес электронной почты получателя письма.",
        required=True
    )

    parser.add_argument(
        "-e",
        help="Название письма. Должно быть ключем в словаре 'emails' в"
             " файле конфигурации 'config.json'. Если ключ не указан -"
             " будет использовано значение по умолчанию '_default'.",
        required=False
    )

    parser.add_argument(
        "-s",
        help="Заголовок письма. Если ключ не указан - будет использовано"
             " значение из файла конфигурации.",
        required=False
    )

    parser.add_argument(
        "-t",
        help="Тип форматирования текста письма. Если ключ не указан"
             " - будет использовано значение из файла конфигурации.",
        required=False
    )

    parser.add_argument(
        "other",
        help="Дополнительные аргументы вида 'ключ=значение'. Будут"
             " использованы для форматирования текста письма.",
        nargs="*"
    )

    return parser.parse_args()
