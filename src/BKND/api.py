from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from configparser import ConfigParser

from ..BTDC import MenestrelBot
from utils.logger import CustomLogger
from .routes import router


class MenestrelApi:
    """This class is the API main class"""

    def __init__(self, config: ConfigParser ,bot: MenestrelBot) -> None:
        self.logger = CustomLogger.get_logger("BKND")
        self.app = FastAPI(title="MenestrelApi",
                           summary="Menestrel Backend API",
                           version=config["API"]["VERSION"])

        self.app.include_router(router)

        self.app.add_middleware(middleware_class=CORSMiddleware,
                                allow_origins=["http://menestrel"],  # Ajouter les domaines autorisés ici
                                allow_credentials=True,
                                allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
                                allow_headers=["*"],  # Autoriser tous les headers
                            )

        self.app.state.bot = bot
        self.config = uvicorn.Config(self.app, host="0.0.0.0", port=int(config["API"]["Port"]), reload=True)
        self.server = uvicorn.Server(self.config)

    async def run(self):
        await self.server.serve()

        
