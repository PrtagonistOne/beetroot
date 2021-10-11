import socket

msgFromClient = 'Hello UDP Server'
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ('127.0.0.1', 20001)
bufferSize = 1024

# Створюємо UDP socket клієнта
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Відправка до сервера через створенний сокет
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = f'Message from Server {msgFromServer[0]}'
print(msg)
