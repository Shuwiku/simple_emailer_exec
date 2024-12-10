# -*- coding: utf-8 -*-
"""Функция, загружающая необходимые параметры из переменных среды."""

import os
import sys
from types import SimpleNamespace
from typing import Optional

from dotenv import load_dotenv
from loguru import logger


def load_argsenv() -> SimpleNamespace:
    """Загружает необходимые параметры из переменных среды.

    Returns:
        SimpleNamespace: Пространство имён с необходимыми переменными.
            Содержит следующие имена: sender_email (str),
            sender_password (str).
    """
    argsenv = SimpleNamespace()
    load_dotenv()

    sender_email: Optional[str] = os.getenv(
        key="SENDER_EMAIL"
    )
    sender_password: Optional[str] = os.getenv(
        key="SENDER_PASSWORD"
    )
    if sender_email is None or sender_password is None:
        logger.error(  # Логирование
            "Адрес электронной почты или пароль приложения не указан!"
        )
        sys.exit()

    argsenv.sender_email = sender_email
    argsenv.sender_password = sender_password

    logger.debug("Параметры из переменных среды загружены")  # Логирование

    return argsenv
