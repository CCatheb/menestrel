import asyncio
from doctest import debug
import discord
import threading
import random
import logging

from queue import Queue
from interface.server import MenestrelApi
from bot.bot import MenestrelBot
from utils.logger import LoggerFactory

discord.utils.setup_logging(level=logging.DEBUG, root=False)

if __name__ == "__main__":

    # Instanciate all needed elements
    logger = LoggerFactory.get_logger("MAIN")

    # See README to find more about these elements
    tasks_queue = Queue()
    data_queue = Queue()

    api = MenestrelApi("MAPI", tasks_queue, data_queue)

    is_running = True
    bot = None
    loop = asyncio.new_event_loop()
    loop.set_debug(True)

    # Start the API in another thread
    flask_thread = threading.Thread(target=api.run)
    flask_thread.start()

    tasks = set()

    while is_running:
        # This is a blocking-like method that waits for an input on the Tasks queue 
        task_entry = tasks_queue.get()
        match task_entry:
            case "RAND":
                # Generate a random int, send it back on the Data queue (to show on the UI)
                value = random.randint(1,100)
                data_queue.put(("0", str(value)))

            case "START_BOT":
                intents = discord.Intents.all()
                bot = MenestrelBot(intents=intents)

                loop.create_task(bot.start_bot())
                loop.run_forever()

                # loop = asyncio.get_event_loop()
                # # loop.create_task(bot.start_bot())
                # loop.call_soon(bot.start_bot)
                # logger.debug("Added bot.start to loop as a task")
                # loop.run_forever()
                logger.info("Bot start asked")
            case "STOP_BOT":
                logger.info("Bot stop asked")
                # FIXME: Task is never called
                loop.create_task(bot.close())
            case "JOIN_VOICE":
                logger.info("Command is to join voice channel")
            case _:
                logger.error("Got a wrong task entry.")

    logger.info("Out of While")

