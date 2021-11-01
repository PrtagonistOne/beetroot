import socket
import asyncio


async def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    loop = asyncio.get_event_loop()

    # Bind the socket to the port
    server_address = ('localhost', 65432)
    print('starting up on {} port {}'.format(*server_address))
    server.bind(server_address)
    server.setblocking(False)
    # Listen for incoming connections
    server.listen(1)
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client = await loop.sock_accept(server)
        try:
            print('connection from ', server.getsockname())
            while True:
                data = await loop.sock_recv(connection, 1024)
                if data:
                    # print(f'\n{connection} {client}')
                    await loop.sock_sendall(connection, data.upper())
                else:
                    break
        except AttributeError as a:
            print(a)
            break

        finally:
            # Clean up the connection
            connection.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
