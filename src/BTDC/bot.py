import discord

from ..LBMG import MusicFinder
from utils.logger import CustomLogger

class MenestrelBot(discord.Client):
    """This is the main class for the bot
    
    Define all methods needed to be executed by the bot on API calls below.
    """

    # TODO: All theses methods should be in a Cog
    # TODO: Add a leave command
    # TODO: Cannot switch music, should add a stop music method
    def __init__(self, config, intents, **options):
        super().__init__(intents=intents, **options)

        self.logger = CustomLogger.get_logger("BTDC")
        self.mf = MusicFinder(config)
        self.config = config


    async def on_ready(self):
        self.logger.info("Bot Ready")
        self.logger.debug(f"Logged as {self.user.name} | {self.user.id}")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!ping"):
            await message.reply("Pong!")

        if message.content == "!join":
            channel = self.get_channel(1219376772236312609)
            await channel.connect()


    async def api_call(self, value):

        channel = self.get_channel(1219376772236312608)
        await channel.send(value)

    async def change_scene(self, scene: str):
        channel = self.get_channel(1219376772236312608)
        result = self.mf.get_music_by_scene(scene)
        await channel.send(result)

        voice_client = discord.utils.get(self.voice_clients)
        audio_source = discord.FFmpegPCMAudio(result, executable=self.config["Discord"]["ffmpeg"])
        voice_client.play(audio_source, after=None)

    async def change_phase(self, phase: str):
        channel = channel = self.get_channel(1219376772236312608)
        result = self.mf.get_music_by_phase(phase)
        await channel.send(result)

        voice_client = discord.utils.get(self.voice_clients)
        audio_source = discord.FFmpegPCMAudio(result, executable=self.config["Discord"]["ffmpeg"])
        voice_client.play(audio_source, after=None)
