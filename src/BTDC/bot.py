import discord

from utils.logger import CustomLogger

class MenestrelBot(discord.Client):

    logger = CustomLogger.get_logger("BTDC")

    async def on_ready(self):
        self.logger.info("Bot Ready")
        self.logger.debug(f"Logged as {self.user.name} | {self.user.id}")

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!ping"):
            await message.reply("Pong!")

    async def api_call(self, value):

        channel = self.get_channel(1219376772236312608)
        await channel.send(value)