import asyncio


async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('-..World')
    return 'Yes'


asyncio.get_event_loop().run_until_complete(main())