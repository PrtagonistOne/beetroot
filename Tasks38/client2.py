import logging
import socket
import asyncio


from config.init_logging import init_logging


async def send_message(connection: socket.socket, message: str) -> None:
    connection.sendall(message.encode())


async def receive_message(connection: socket.socket) -> None:
    data = connection.recv(1024)
    print(data.decode())


async def run_client(host: str, port: int):
    logging.info('run_client')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        logging.info(f'Connection to server: {host=} {port=}')
        conn.connect((host, port))
        logging.info('connected')
        print("(If wish to quite input \'q\')\n")
        while True:
            message = input(': ')
            if message == 'q':
                break
            await send_message(connection=conn, message=message)
            await receive_message(connection=conn)


async def main():
    host = '127.0.0.1'
    port = 65432

    await run_client(host=host, port=port)


if __name__ == '__main__':
    init_logging()
    asyncio.run(main())
