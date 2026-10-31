from phoenix import Phoenix


def test_orchestrator_loads_config():
    p = Phoenix("config/device.json")
    assert p.config is not None
    assert "server" in p.config


def test_orchestrator_has_client():
    p = Phoenix("config/device.json")
    assert p.client is not None


def test_orchestrator_has_pipeline():
    p = Phoenix("config/device.json")
    assert p.pipeline is not None


def test_orchestrator_has_audio_manager():
    p = Phoenix("config/device.json")
    assert p.audio is not None


def test_orchestrator_has_screen():
    p = Phoenix("config/device.json")
    assert p.screen is not None


def test_orchestrator_starts_not_running():
    p = Phoenix("config/device.json")
    assert p.running is False
