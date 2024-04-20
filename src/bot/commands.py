import discord, os

from discord.ext import commands
from utils.logger import LoggerFactory


# TODO: Find a better way to set these variables
BASE_PATH = "/home/gabrog/git/Python/Menestrel"
logger = LoggerFactory.get_logger("BOT_CMD")

@commands.command()
async def test(ctx):
    await ctx.send(f'Hello {ctx.author.display_name}')

@commands.command()
async def join(ctx):
    logger.info(f"Received command 'join' from user {ctx.author.display_name}")
    try:
        channel = ctx.author.voice.channel
        logger.info("Connecting bot...")
        logger.debug(f"Trying to join channel '{channel}'")

        await channel.connect()

        logger.debug(f"Joined channel '{channel}'")
        logger.info("Bot connected.")
    except Exception as e:
        logger.warning(f"Menestrel could not join voice channel:\n{e}")
        await ctx.send("Menestrel ne s'est pas réveillé ce matin...")

@commands.command()
async def play(ctx, url):

    logger.info(f"Received command 'play' from user {ctx.author.display_name} with url={url}")

    # Get the bot actual voice client
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        logger.warning("Command 'play' invoked meanwhile Menestrel is not connected.")
        await ctx.send("Menestrel a décidé de ne pas se joindre à vous...")
        return

    if voice_client.is_connected():
        file_path = os.path.join(BASE_PATH, f"sounds/musics/{url}.mp3")
        if os.path.isfile(file_path):
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=file_path))
            logger.info(f"Menestrel playing: {file_path}")
        else:
            logger.warning(f"Music '{file_path}' not found.")
            await ctx.send(f"Music '_{file_path}_' not found.")
    else:
        logger.warning("Command 'play' called but Menestrel is not in any vocal.")
        await ctx.send("Menestrel vous boude. Il réclame son salaire...")

@commands.command()
async def pause(ctx):

    logger.info(f"Received command 'pause' from user {ctx.author.display_name}")

    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        logger.debug("Menestrel paused playing music.")
    else:
        await ctx.send("Menestrel ne jouait pas de musique...")

@commands.command()
async def resume(ctx):

    logger.info(f"Received command 'resume' from user {ctx.author.display_name}")

    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        logger.debug("Menestrel resumed playing music.")
    else:
        await ctx.send("Menestrel ne jouait pas de musique...")

@commands.command()
async def pause(ctx):

    logger.info(f"Received command 'pause' from user {ctx.author.display_name}")

    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        logger.debug("Menestrel paused playing music.")
    else:
        await ctx.send("Menestrel ne jouait pas de musique...")

@commands.command()
async def resume(ctx):

    logger.info(f"Received command 'resume' from user {ctx.author.display_name}")

    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        logger.debug("Menestrel resumed playing music.")
    else:
        await ctx.send("Menestrel ne jouait pas de musique...")

@commands.command()
async def stop(ctx):

    logger.info(f"Received command 'stop' from user {ctx.author.display_name}")

    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        logger.debug("Menestrel stopped playing.")
    else:
        await ctx.send("Menestrel ne jouait pas de musique...")

@commands.command()
async def leave(ctx):
    logger.info(f"Received command 'leave' from user {ctx.author.display_name}")
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        logger.debug("Disconnecting bot from voice")
        await voice_client.disconnect()
        logger.info("Menestrel is now disconnected from voice.")
    else:
        logger.warn("Menestrel is not currently connected to any voice channel.")

async def setup(bot):

    bot.add_command(test)
    bot.add_command(join)
    bot.add_command(leave)
    bot.add_command(play)
    bot.add_command(stop)
    bot.add_command(pause)
    bot.add_command(resume)
    logger.info("Commands loaded")