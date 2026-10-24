from __future__ import annotations

from pydantic import BaseModel, Field


class ServerConfig(BaseModel):
    url: str
    user: str
    password: str


class VoiceConfig(BaseModel):
    wake_phrase: str = Field(default="hey phoenix")
    default_seek_seconds: int = Field(default=15, ge=1, le=300)


class DisplayConfig(BaseModel):
    brightness_idle: int = Field(default=30, ge=0, le=100)
    brightness_playing: int = Field(default=70, ge=0, le=100)


class DeviceConfig(BaseModel):
    server: ServerConfig
    voice: VoiceConfig
    display: DisplayConfig


def validate_device_config(data: dict) -> dict:
    """Validate and return the device configuration dict."""
    cfg = DeviceConfig(**data)
    return cfg.model_dump()
