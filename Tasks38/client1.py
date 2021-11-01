import asyncio


async def echo_client1():
    reader, writer = await asyncio.open_connection(
        'localhost', 65432)
    print("(If wish to quite input \'q\')\n")
    while True:
        # print(f'Send: {message!r}')
        message = input('')
        if message != 'q':
            writer.write(message.encode())

            data = await reader.read(100)
            print(f'{data.decode()!r}')
        else:
            #   print('Close the connection')
            writer.close()
            break


if __name__ == '__main__':
    asyncio.run(echo_client1())
