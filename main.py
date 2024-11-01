from BKND import MenestrelApi

import asyncio

async def main():
    api = MenestrelApi()
    await asyncio.gather(api.run())

if __name__ == "__main__":
    asyncio.run(main())
    