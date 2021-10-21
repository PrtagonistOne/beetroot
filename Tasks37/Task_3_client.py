import asyncio
from Task_3 import client_main


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(client_main())
