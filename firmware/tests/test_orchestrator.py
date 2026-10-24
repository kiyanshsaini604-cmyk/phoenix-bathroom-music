import asyncio

import phoenix


def test_orchestrator_loads_config():
    p = phoenix.Phoenix("config/device.json")
    assert p.config is not None
    assert "server" in p.config


def test_orchestrator_has_client():
    p = phoenix.Phoenix("config/device.json")
    assert p.client is not None


def test_orchestrator_has_pipeline():
    p = phoenix.Phoenix("config/device.json")
    assert p.pipeline is not None


def test_orchestrator_has_audio_manager():
    p = phoenix.Phoenix("config/device.json")
    assert p.audio is not None


def test_orchestrator_has_screen():
    p = phoenix.Phoenix("config/device.json")
    assert p.screen is not None


def test_orchestrator_starts_not_running():
    p = phoenix.Phoenix("config/device.json")
    assert p.running is False
