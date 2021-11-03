import logging, asyncio

from config.init_logging import init_logging
from config.loggers import get_core_logger, get_connection_logger
from server.start_server import start_server
from shared.typing import T_CLIENT_ADDRESS, T_CONNECTION, T_CONNECTIONS


async def handle_connection(conn: T_CONNECTION, client_address: T_CLIENT_ADDRESS, clients: T_CONNECTIONS):
    logger = get_connection_logger(name=str(client_address))
    clients.append(conn)
    loop = asyncio.get_event_loop()

    try:
        logger.info(f'connection from {client_address}')
        messages = []
        # Получення даних та передача їх всім клієнтам
        while True:
            message = (await loop.sock_recv(conn, 1024)).decode().upper()
            messages.append(message)
            logger.info(f'received {len(messages)} messages from {len(clients)} clients')

            if message:
                logger.info('sending data to the clients')

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
        logging.info('waiting for a connetion')
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