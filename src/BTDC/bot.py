import discord

from utils.logger import CustomLogger

class MenestrelBot(discord.Client):

    logger = CustomLogger.get_logger("BTDC")

    async def on_ready(self):
        self.logger.info("Bot Ready")
        self.logger.debug(f"Logged as {self.user.name} | {self.user.id}")