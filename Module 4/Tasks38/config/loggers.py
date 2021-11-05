import logging


def get_core_logger() -> logging.Logger:
    return  logging.getLogger()


def get_connection_logger(name: str) -> logging.Logger:
    return logging.getLogger(f'connection: [{name}]')