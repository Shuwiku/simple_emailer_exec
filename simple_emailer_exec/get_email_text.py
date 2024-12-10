# -*- coding: utf-8 -*-
"""Получает текст письма, и при необходимости форматирует его."""

from pathlib import Path

from jinja2 import Template
from loguru import logger


def get_email_text(
    email_data: dict,
    other_args: dict
) -> str:
    """Получает текст письма, и при необходимости форматирует его.

    Args:
        email_data (dict): Данные о письме из файла конфигурации.
        other_args (list[str]): Дополнительные аргументы из командой строки.

    Returns:
        str: Текст письма.
    """
    email_file_path: Path = Path("emails").resolve() / email_data["filename"]

    with open(email_file_path, mode="r", encoding="utf-8") as f:
        email_text: str = f.read()
        logger.debug("Текст письма получен.")  # Логирование

    if email_data["with_args"]:
        jinja_template = Template(email_text)
        email_text: str = jinja_template.render(other_args)
        logger.debug("Текст письма отформатирован.")  # Логирование

    return email_text
