from flask import Flask, render_template, request
import os
from queue import Queue
from utils.logger import LoggerFactory


class MenestrelApi:

    def __init__(self, name: str, tasks_queue: Queue, data_queue: Queue) -> None:
        
        self.logger = LoggerFactory.get_logger(name)

        self.logger.info("Menestrel API initialisation")

        static_folder = os.path.join(os.getcwd() + "/interface/templates/static")
        self.logger.info(f"Looking for templates, CSS and JS files at '{static_folder}'")

        self.app = Flask(__name__, static_folder=static_folder)
        self.app.logger.handlers = []
        for hdlr in self.logger.handlers:
            self.app.logger.addHandler(hdlr)

        self.task_queue = tasks_queue
        self.data_queue = data_queue
        self.configure_routes()
        
    def __check_command(self):
        """This method checks the reponse of a command in the data queue, and return data if needed to the UI.

        Returns:
            tuple(str, int): Tuple with the command result and the HTTP-like response code
        """
        self.logger.debug(f"Waiting for response")
        response = self.data_queue.get()
        if response[0] == "0":
            self.logger.info(f"Command succeeded. Got response '{response[1]}'")
            return response[1], 200
        else:
            self.logger.warning("No response received")
            return "", 500

    def configure_routes(self):
        """Generates the routes for the API. Each route must set a task in the queue.

        Returns:
            tuple(str, int): Tuple with the command result and the HTTP-like response code
        """

        self.logger.info("Configuring routes")
        @self.app.route("/", methods=["GET"])
        def hello_world():
            return render_template("index.html")

        @self.app.route("/number", methods=["GET"])
        def generate_random_number():
            self.task_queue.put("RAND")
            return self.__check_command()

        @self.app.route("/start", methods=["GET"])
        def start_menestrel():
            self.logger.info("Start Menestrel Bot asked...")
            self.task_queue.put("START_BOT")
            return self.__check_command()
        
        @self.app.route("/stop", methods=["GET"])
        def stop_menestrel():
            self.logger.info("Stop Menestrel Bot asked...")
            self.task_queue.put("STOP_BOT")
            return self.__check_command()
        
        @self.app.route("/join-voice", methods=["GET"])
        def join_voice():
            self.logger.info("Menestrel join voice")
            self.task_queue.put("JOIN_VOICE")
            return self.__check_command()
        
        self.logger.info("Routes configured")

    def run(self):
        """Run the API"""
        
        self.logger.info("Mestrel API is starting...")
        self.app.run(port=12345, debug=True, use_reloader=False)