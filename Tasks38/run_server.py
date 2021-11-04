import asyncio
import logging
import enum
import uuid
from datetime import datetime
from config.init_logging import init_logging
from config.loggers import get_core_logger, get_connection_logger
from server.start_server import start_server
from shared.typing import T_CLIENT_ADDRESS, T_CONNECTION, T_CONNECTIONS

COMMAND_PREFIX = '/'


@enum.unique
class Commands(enum.Enum):
    HELP = 'help'
    QUIT = 'quit'
    RENAME = 'rename'


def handle_command__help() -> str:
    return 'For more info, go learn SQL instead.. \nIf you wish to change your nickname use "/rename <nickname>"\n' \
           'If you wish to leave type "/quit"'


def handle_command__quit() -> str:
    return '>?>?././Permission to leave<>><><@'


commands_handlers = {
    Commands.HELP: handle_command__help,
    Commands.QUIT: handle_command__quit,
}


def handle_message(message: str):
    if message.startswith('/rename'):
        return message

    if not message.startswith(COMMAND_PREFIX):
        return message

    command_raw = message.replace(COMMAND_PREFIX, '', 1)
    try:
        command = Commands(command_raw)
    except ValueError:
        return f'This is bad command: {message}. Available commands is: "{",".join([x.value for x in Commands])}"'

    return commands_handlers[command]()


def format_message(message: str, name: str) -> str:
    time = datetime.now()
    return f'[{time.hour}:{time.minute}:{time.second}][{name}]: {message}'


async def handle_connection(conn: T_CONNECTION, client_address: T_CLIENT_ADDRESS, clients: T_CONNECTIONS):
    logger = get_connection_logger(name=str(client_address))
    clients.append(conn)
    loop = asyncio.get_event_loop()
    name = uuid.uuid4().hex
    try:
        logger.info(f'connection from {client_address}')
        messages = []
        # Получення даних та передача їх всім клієнтам
        while True:
            message = (await loop.sock_recv(conn, 1024)).decode()
            messages.append(message)
            logger.info(f'received {len(messages)} messages from {len(clients)} clients')

            if message:
                logger.info('sending data to the clients')
                message = handle_message(message=message)
                if message == '>?>?././Permission to leave<>><><@':
                    break
                if message.startswith('/rename'):
                    name = message.split()[1]
                    message = f'Name was changed to {name} successfully!'
                message = format_message(message=message, name=name)
                message_to_send = message.encode()

                # for client in clients:
                #     await loop.sock_sendall(client, message_to_send)

                await asyncio.gather(
                    *[loop.sock_sendall(client_socket, message_to_send) for client_socket in clients]
                )

                logger.info('data sent to the clients')

            else:
                logger.info('no data from', client_address)
                break

    except ConnectionError as exc:
        logging.exception(exc)

    finally:
        clients.remove(conn)
        conn.close()
        logger.info('connection closed')


async def handle_connections(server: T_CONNECTION):
    clients = []
    loop = asyncio.get_event_loop()
    while True:
        logging.info('waiting for a connection')
        connection, client_address = await loop.sock_accept(server)
        logging.info('connection accepted')
        loop.create_task(handle_connection(
            conn=connection,
            client_address=client_address,
            clients=clients
        ))


async def main():
    host = '127.0.0.1'
    port = 65432

    logger = get_core_logger()
    logger.info('start app')

    server = start_server(host=host, port=port)
    await handle_connections(server=server)

    logger.info('finish app')


if __name__ == '__main__':
    init_logging()
    asyncio.run(main())
