from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.logger import CustomLogger

router = APIRouter()
logger = CustomLogger.get_logger("RTES")

class Validator(BaseModel):
    value: str

@router.post("/scene")
async def scene(scene: Validator):
    logger.info("scene " + scene.value)

@router.post("/phase")
async def phase(phase: Validator):
    logger.info("phase " + phase.value)

@router.post("/meteo")
async def meteo(meteo: Validator):
    logger.info("meteo " + meteo.value)

@router.post("/ambiance")
async def ambiance(ambiance: Validator):
    logger.info("ambiance " + ambiance.value)

@router.post("/sfx")
async def sfx(sfx: Validator):
    logger.info("sfx " + sfx.value)

@router.post("/general")
async def general(action: Validator):
    logger.info("action " + action.value)