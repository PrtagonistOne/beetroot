import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

loop = asyncio.get_event_loop()

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.setblocking(False)
# Listen for incoming connections
sock.listen(1)


async def main():
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client = await loop.sock_accept(sock)
        try:
            print('connection from ', sock.getsockname())
            while True:
                data = await loop.sock_recv(connection, 1024)
                print('sending data back to the clients')
                await loop.sock_sendall(client, data)
        except:
            print('no data from', client)
            break

        finally:
            # Clean up the connection
            connection.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
