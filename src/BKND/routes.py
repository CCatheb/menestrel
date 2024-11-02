from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from utils.logger import CustomLogger

router = APIRouter()
logger = CustomLogger.get_logger("RTES")

class Validator(BaseModel):
    value: str

@router.post("/scene")
async def scene(request: Request, scene: Validator):
    text = "Scene - " + scene.value
    logger.info(text)
    bot = request.app.state.bot
    await bot.change_scene(scene.value)

@router.post("/phase")
async def phase(request: Request, phase: Validator):
    text = "Phase - " + phase.value
    logger.info(text)
    bot = request.app.state.bot
    await bot.api_call(text)

@router.post("/meteo")
async def meteo(request: Request, meteo: Validator):
    text = "Meteo - " + meteo.value
    logger.info(text)
    bot = request.app.state.bot
    await bot.api_call(text)

@router.post("/ambiance")
async def ambiance(request: Request, ambiance: Validator):
    text = "Ambiance - " + ambiance.value
    logger.info(text)
    bot = request.app.state.bot
    await bot.api_call(text)

@router.post("/sfx")
async def sfx(request: Request, sfx: Validator):
    text = "SFX - " + sfx.value
    logger.info(text)
    bot = request.app.state.bot
    await bot.api_call(text)

@router.post("/general")
async def general(request: Request, action: Validator):
    text = "General - " + action.value
    logger.info(text)
    bot = request.app.state.bot
    await bot.api_call(text)