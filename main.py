import discord
from src.BKND import MenestrelApi
from src.BTDC import MenestrelBot

import asyncio
import configparser

def load_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    return config

async def main():

    config = load_config()
    
    bot = MenestrelBot(config, intents=discord.Intents.all())
    api = MenestrelApi(config, bot)
    await asyncio.gather(api.run(),
                        bot.start(config["Discord"]["Token"]))

if __name__ == "__main__":
    asyncio.run(main())
