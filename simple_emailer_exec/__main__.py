# -*- coding: utf-8 -*-
"""Simple Emailer Exec - утилита для отправки писем через SMTP Gmail."""

from argparse import Namespace
from types import SimpleNamespace

from loguru import logger
from simple_emailer import SimpleEmailerError, send_email_quick

from args import load_args
from args_parser import parse_args
from argsenv import load_argsenv
from config import load_config
from get_email_text import get_email_text
from setup_logging import setup_logging


def main() -> None:
    """If __name__ == "__main__"."""
    parsed_args: Namespace = parse_args()

    config: SimpleNamespace = load_config()

    setup_logging(
        logging_config=config.logging
    )

    args: SimpleNamespace = load_args(
        email_config=config.emails,
        parsed_args=parsed_args
    )
    argsenv: SimpleNamespace = load_argsenv()

    email_text = get_email_text(
        email_data=config.emails[args.email_name],
        other_args=args.other
    )

    try:
        send_email_quick(
            email_text=email_text,
            recipient_email=args.recipient_email,
            sender_email=argsenv.sender_email,
            sender_password=argsenv.sender_password,
            subject=args.email_subject,
            email_type=args.email_type
        )
        logger.info("Письмо успешно отправлено.")  # Логирование
    except SimpleEmailerError as e:
        logger.error(e)  # Логирование


if __name__ == "__main__":
    main()
