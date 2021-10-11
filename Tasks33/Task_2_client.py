import socket


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
