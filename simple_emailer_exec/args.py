# -*- coding: utf-8 -*-
"""Функция, обрабатывающая аргументы, переданные из командной строки."""

from argparse import Namespace
from types import SimpleNamespace
from typing import Optional

from loguru import logger


def load_args(
    email_config: dict,
    parsed_args: Namespace
) -> SimpleNamespace:
    """Обрабатывает аргументы, переданные из командной строки.

    Args:
        email_config (dict): Конфигурация писем из файла конфигурации.

    Returns:
        SimpleNamespace: Простанство имён с обработанными аргументами.
            Содержит следующие имена: email_name (str), email_subject (str),
            email_type (str), recipient_email (str), other (dict).
    """
    args = SimpleNamespace()

    email_name: Optional[str] = parsed_args.e
    if email_name is None:
        email_name = email_config["_default"]
    logger.debug(f"Отправляемое письмо: '{email_name}'.")  # Логирование
    args.email_name = email_name

    email_subject: Optional[str] = parsed_args.s
    if email_subject is None:
        email_subject = email_config[email_name]["subject"]
    else:
        # Логирование
        logger.debug(f"Иное значение для параметра: {email_subject=}")
    args.email_subject = email_subject

    email_type: Optional[str] = parsed_args.t
    if email_type is None:
        email_type = email_config[email_name]["type"]
    else:
        # Логирование
        logger.debug(f"Иное значение для параметра: {email_type=}")
    args.email_type = email_type

    args.recipient_email = parsed_args.r

    other_args: list[str] = parsed_args.other
    new_other_args: dict = {}
    for i in other_args:
        data: list[str] = i.split("=")
        if len(data) == 2:
            new_other_args[data[0]] = data[1]
            # Логирование
            logger.debug(f"Дополнительный параметр: {data[0]} = {data[1]}")
    args.other = new_other_args

    logger.debug("Аргументы командной строки обработаны.")  # Логирование

    return args
