import socket

localIP = '127.0.0.1'
localPort = 20001
bufferSize = 1024

msgFromServer = 'Hello UDP Client!'
bytesToSend = str.encode(msgFromServer)

# Створюємо датаграм сокэт
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Прив'язка до адресу та порту
UDPServerSocket.bind((localIP, localPort))

print(f'UDP server up and listening on {localIP}:{localPort}')

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = f'Message from Client: {message}'
    clientIP = f'Client IP Address: {address}'

    print(clientMsg)
    print(clientIP)

    # Відправка відповіді клієнту
    UDPServerSocket.sendto(bytesToSend, address)
