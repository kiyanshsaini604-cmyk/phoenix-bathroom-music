import pytest
import asyncio
import phoenix.config
import phoenix.music
import phoenix.voice
import phoenix.ui


@pytest.fixture
def config():
    return phoenix.config.load("config/device.json")


@pytest.fixture
def music_client(config):
    return phoenix.music.Client(config["server"])


@pytest.fixture
def voice_pipeline(config):
    return phoenix.voice.Pipeline(config["voice"])


@pytest.fixture
def ui():
    return phoenix.ui.Screen()
