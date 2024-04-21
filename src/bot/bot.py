import discord
import asyncio
import os
import configparser

from utils.logger import LoggerFactory

class MenestrelBot(discord.Client):

    def __init__(self, intents: discord.Intents,) -> None:
        super().__init__(intents=intents)

        self.logger = LoggerFactory.get_logger("MBOT")
        self._load_bot_configuration()

    async def on_ready(self):
        self.logger.debug(f"Logged in as {self.user}")

        self.loop = asyncio.get_running_loop()

        # Set the bot as invisible
        await self.change_presence(status=discord.Status.invisible)

        self.logger.debug("Available guilds and channels are:")
        for guild in self.guilds:
            self.logger.debug(f"\t- {guild}")
            for channel in guild.voice_channels:
                self.logger.debug(f"\t\t- {channel}")

    def get_loop(self):
        return self.loop

    async def setup_hook(self) -> None:
        # TODO
        pass 

    async def start_bot(self):
        await self.login(self.token)
        self.logger.debug("Login to Discord API Done")
        await self.connect()
        self.logger.info("Bot started")

    def _load_bot_configuration(self):
        """Load the configuration of the bot from conf.ini file"""

        config_file = os.path.join(os.path.dirname(os.getcwd()), 'conf/conf.ini')

        self.logger.debug(f"Loading configuration from file {config_file}")
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.config = self.config["DISCORD"]

        self.token = self.config.get("TOKEN")
        self.logger.info("Loaded configuration")
