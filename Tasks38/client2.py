import logging
import socket
from threading import Thread


from config.init_logging import init_logging
from shared.typing import T_CONNECTION


def send_message(connection: socket.socket) -> None:
    print('for the list of commands type "/help"')
    while True:
        message = input(': ')
        connection.sendall(message.encode())
        if message == '/quit':
            exit()


def display_message(message: str) -> None:
    print(message)


def receive_message(connection: socket.socket) -> None:
    while True:
        data = connection.recv(1024)
        if data.decode() == "":
            exit()
        display_message(data.decode())


def handle_connection(connection: T_CONNECTION) -> None:
    Thread(
        target=receive_message,
        args=(connection,),
        daemon=True,
    ).start()
    send_message(connection=connection)



def run_client(host: str, port: int):
    logging.info('run_client')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        logging.info(f'Connection to server: {host=} {port=}')
        conn.connect((host, port))
        logging.info('connected')

        handle_connection(connection=conn)


def main():
    host = '127.0.0.1'
    port = 65432

    run_client(host=host, port=port)


if __name__ == '__main__':
    init_logging()
    main()
