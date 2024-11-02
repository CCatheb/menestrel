from configparser import ConfigParser
from tinydb import TinyDB, Query, where
import random
import os

from utils.logger import CustomLogger

class MusicFinder:
    """This class is the part of the bot in charge of finding a sound element matching the requested scene/phase/etc"""

    def __init__(self, config: ConfigParser):

        self.logger = CustomLogger.get_logger("LBMG")

        db_path = os.path.join(os.getcwd(), "data", config["Database"]["File"])

        self.logger.debug(f"Searching database at: {db_path}")
        if os.path.isfile(db_path):
            self.db = TinyDB(db_path)
            self.logger.info("Database found")
        else:
            self.logger.error("Database not found at given path")

        self.scene = ""
        self.phase = ""
        self.meteo = {
            "Pluie":0,
            "Orage":0,
            "Vent":0 
        }
        self.ambiance = {
            "Rivière":0,
            "Cascade":0,
            "Vague":0,
            "Murmures":0,
            "Feu de camp":0,
            "Cigales":0
        }
        self.sfx = ""

    def get_music_by_scene(self, scene: str) -> str:
        """This method finds all musics matching given scene.
        Chooses one randomly if multiple results are given.

        Args:
            scene (str): Asked scene

        Returns:
            str: Path to the music
        """
        Audio = Query()

        self.scene = scene

        if not self.phase:
            self.logger.info("No phase have been set, defaults to 'Exploration'")
            self.phase = "Exploration"

        self.logger.debug(f"Serching music for scene = {scene} and phase = {self.phase}")
        result = self.db.search(
            (Audio.type == 'music') &
            (Audio.tags['scene'] == scene) &
            (Audio.tags['phase'] == self.phase)
        )

        if result:
            return random.choice(result)["path"]

        self.logger.warning("No music found for specified scene and phase.")
        return "Not found"
    
    def get_music_by_phase(self, phase: str) -> str:
        """This method finds all musics matching given phase.
        Chooses one randomly if multiple results are given.

        Args:
            phase (str): Asked phase

        Returns:
            str: Path to the music
        """
        Audio = Query()

        if not self.scene:
            self.logger.info("No scene have been set, defaults to 'Ville'")
            self.scene = "Ville"

        self.phase = phase

        self.logger.debug(f"Serching music for scene = {phase} and phase = {self.phase}")
        result = self.db.search(
            (Audio.type == 'music') &
            (Audio.tags['scene'] == self.scene) &
            (Audio.tags['phase'] == phase)
        )

        if result:
            return random.choice(result)["path"]

        self.logger.warning("No music found for specified scene and phase.")
        return "Not found"