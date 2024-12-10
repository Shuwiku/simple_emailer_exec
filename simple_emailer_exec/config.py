# -*- coding: utf-8 -*-
"""Docstring."""

import json
from pathlib import Path
from types import SimpleNamespace


def load_config() -> SimpleNamespace:
    """Загружает данные из файла конфигурации.

    Returns:
        SimpleNamespace: Пространство имён с конфигурацией бота.
            Содержит следующие имена: emails (dict), logging (dict).
    """
    config = SimpleNamespace()

    config_path: Path = Path("config.json").resolve()
    with open(
        file=config_path,
        mode="r",
        encoding="utf-8"
    ) as f:
        config_data: dict = json.load(f)

    config.emails = config_data["emails"]
    config.logging = config_data["logging"]

    return config
