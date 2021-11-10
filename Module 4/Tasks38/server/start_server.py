import logging
import socket

from shared.typing import T_HOST, T_PORT


def start_server(host: T_HOST, port: T_PORT, max_unaccepted_conn: int = 0) -> socket.socket:
    # Створюємо TCP/IP socket for
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info(f'starting up on {host=} {port=}')
    server.bind((host, port))
    server.listen(max_unaccepted_conn)
    server.setblocking(False)

    logging.info(f'started on {host=} {port=}')
    return server
