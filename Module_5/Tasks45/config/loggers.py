import logging


def get_core_logger() -> logging.Logger:
    return logging.getLogger('core')


def get_message_logger() -> logging.Logger:
    return logging.getLogger('message')
