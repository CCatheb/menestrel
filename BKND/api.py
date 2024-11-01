from fastapi import FastAPI
import uvicorn

from utils.logger import CustomLogger
from .routes import router


class MenestrelApi:
    """This class is the API main class"""

    VERSION = "1"

    def __init__(self) -> None:
        self.logger = CustomLogger.get_logger("BKND")
        self.app = FastAPI(title="MenestrelApi",
                           summary="Menestrel Backend API",
                           version=self.VERSION)

        self.app.include_router(router)

    def run(self):
        uvicorn.run(app=self.app,
                    host="192.168.0.33",
                    port=8000)
