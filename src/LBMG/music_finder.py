from configparser import ConfigParser
from genericpath import isfile
from typing import List, Optional, Dict
from tinydb import TinyDB, Query, where
import random
import os

from utils.logger import CustomLogger

class MusicFinder:

    def __init__(self, config: ConfigParser):

        self.logger = CustomLogger.get_logger("LBMG")

        db_path = os.path.join(os.getcwd(), "data", config["Database"]["File"])

        self.logger.debug(f"Searching database at: {db_path}")
        if os.path.isfile(db_path):
            self.db = TinyDB(db_path)
            self.logger.info("Database found")
        else:
            self.logger.error("Database not found at given path")

    def get_music(self, scene: str, phase: str) -> Optional[Dict]:
        Audio = Query()
        
        self.logger.debug(f"Serching music for scene = {scene} and phase = {phase}")
        result = self.db.search(
            (Audio.type == 'music') &
            (Audio.tags['scene'] == scene) &
            (Audio.tags['phase'] == phase)
        )

        if result:
            return random.choice(result)

        self.logger.warning("No music found for specified scene and phase.")
        return None