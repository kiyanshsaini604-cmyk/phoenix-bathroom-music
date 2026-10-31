import pytest
import asyncio
import phoenix.voice
import phoenix.schemas
from phoenix import Pipeline, DeviceConfig, AudioManager, MusicClient, Screen
from phoenix.config import load


@pytest.fixture
def config():
    return load("config/device.json")


@pytest.fixture
def music_client(config):
    return MusicClient(config["server"]["url"], config["server"]["user"], config["server"]["password"])


@pytest.fixture
def voice_pipeline(config):
    return Pipeline(config["voice"])


@pytest.fixture
def ui():
    return Screen()
