import phoenix.config


def test_load_returns_dict():
    cfg = phoenix.config.load("config/device.json")
    assert isinstance(cfg, dict)


def test_server_section_present(config):
    assert "server" in config
    assert "url" in config["server"]


def test_voice_section_present(config):
    assert "voice" in config
    assert "default_seek_seconds" in config["voice"]
    assert config["voice"]["default_seek_seconds"] == 15
