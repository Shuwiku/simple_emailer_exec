# -*- coding: utf-8 -*-
"""Функция, настраивающая логирование."""

import sys
from pathlib import Path

from loguru import logger


def setup_logging(
    logging_config: dict
) -> None:
    """Настаивает логирование.

    Args:
        logging_config (dict): Конфигурация логирования из файла конфигурации.
    """
    logger.remove()
    logger.add(
        format=logging_config["format_std"],
        level=logging_config["level"],
        sink=sys.stderr
    )
    logger.add(
        format=logging_config["format_file"],
        level=logging_config["level"],
        sink=Path(logging_config["file_name"])
    )
    logger.debug("Логирование настроено.")  # Логирование
