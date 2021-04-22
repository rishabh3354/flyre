import json
from pathlib import Path

__all__ = ["Settings", "settings"]

from .constants import ASSETS_DIR


class Settings:
    """
    A singleton for all the settings that can be saved and loaded from the disk.

    Every attribute that is set in the __init__ will be saved and restored with :load: and :save:.
    """

    _instance = None
    from pathlib import Path
    PATH = str(Path.home()) + "/settings.json"

    # PATH = ASSETS_DIR / "settings.json"

    def __new__(cls):
        if cls._instance:
            return cls._instance

        # create the only instance of cls
        self = super(Settings, cls).__new__(cls)
        cls._instance = self
        # Then we set the defaults and load it from the disk
        cls.__init__(self)
        self.load()
        # Finaly we swap __init__ and reset, so it will not be rest
        # Every time Settings() is called, as __init__ is always called after __new__.
        cls.reset = cls.__init__
        cls.__init__ = lambda s: None

        return self

    def __init__(self):
        self.debug = False
        self.highscores = []
        self.name = "Cool kid"
        self.last_score = None
        self.mute = False

    def load(self):
        """(re)load the settings from the file. Called automatically on the first instance of Settings."""

        # if self.PATH.exists():
        #     self.__dict__.update(json.loads(self.PATH.read_text()))
        if self.PATH:
            try:
                user_data_file = open(self.PATH, "r+")
                data = user_data_file.read()
                self.__dict__.update(json.loads(data))
            except Exception as e:
                default = {"debug": False,
                           "highscores": [[15000, "Warlord"], [8900, "F\u00e9lix"], [3000, "Daniel"]],
                           "name": "Alan Walker",
                           "last_score": [3000, "Robert"], "mute": False}
                data = json.dumps(default)
                with open(self.PATH, "w+") as file:
                    file.write(data)

    def save(self):
        """Save the settings to its file. This is not called automatically."""

        # self.PATH.write_text(json.dumps(self.__dict__))
        data = json.dumps(self.__dict__)
        with open(self.PATH, "w+") as file:
            file.write(data)

    def reset(self):
        """Reset the settings."""


settings = Settings()
