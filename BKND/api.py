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
        self.config = uvicorn.Config(self.app, host="0.0.0.0", port=8000, reload=True)
        self.server = uvicorn.Server(self.config)

    async def run(self):
        await self.server.serve()

        
