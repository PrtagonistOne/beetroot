import threading
import socket


class ServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', 65432)
        print('starting up on {} port {}'.format(*server_address))
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)

        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()
            try:
                print('connection from', client_address)

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(1024)
                    print('received {!r}'.format(data))
                    if data:
                        print('sending data back to the client')
                        connection.sendall(data.upper())
                    else:
                        print('no data from', client_address)
                        break

            finally:
                # Clean up the connection
                connection.close()


class ClientThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        def encrypt(text, s):
            result = ""
            # transverse the plain text
            for i in range(len(text)):
                char = text[i]
                # Encrypt uppercase characters in plain text

                if char.isupper():
                    result += chr((ord(char) + s - 65) % 26 + 65)
                # Encrypt lowercase characters in plain text
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            return result

        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 65432  # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            message = encrypt(input('Input the text to encrypt: ').upper(), int(input('Input the key(digits only): ')))
            s.sendall(bytes(message, 'ascii'))
            data = s.recv(1024)

        print('Received', data)


if __name__ == '__main__':
    ServerThread1 = ServerThread()
    ServerThread1.start()

