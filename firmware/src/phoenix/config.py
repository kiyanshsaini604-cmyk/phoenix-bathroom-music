import json
from pathlib import Path

from phoenix import schemas


def load(path: str | Path = "config/device.json") -> dict:
    """Load the device configuration from a JSON file."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return schemas.validate_device_config(data)


def default() -> dict:
    """Return a minimal default configuration."""
    return {
        "server": {
            "url": "http://music.local:4040",
            "user": "user",
            "password": "changeme",
        },
        "voice": {
            "wake_phrase": "hey phoenix",
            "default_seek_seconds": 15,
        },
        "display": {
            "brightness_idle": 30,
            "brightness_playing": 70,
        },
    }
