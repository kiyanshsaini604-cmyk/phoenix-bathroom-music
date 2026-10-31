import logging
from dataclasses import dataclass
from typing import Any

LOG = logging.getLogger("phoenix.ui")


class DeviceState:
    IDLE = "idle"
    LISTENING = "listening"
    RECOGNIZED = "recognized"
    PLAYING = "playing"
    PAUSED = "paused"
    NO_MATCH = "no_match"
    SEEK = "seek"


@dataclass
class TouchEvent:
    kind: str


class Screen:
    def __init__(self):
        self.state = "idle"
        self._pending_touch: TouchEvent | None = None
        self._last_track: dict[str, Any] | None = None
        self._last_seek: int = 0
        self._play_state: bool = False

    def show_state(self, state: str):
        LOG.info("Showing state: %s", state)
        self.state = state
        if state == "playing":
            self._play_state = True
        elif state in ("paused",):
            self._play_state = False

    def show_idle(self):
        self.show_state("idle")

    def show_listening(self):
        self.show_state("listening")

    def show_recognized(self):
        self.show_state("recognized")

    def show_playing(self, track: dict[str, Any] | None = None):
        self._last_track = track
        self.show_state("playing")

    def show_paused(self):
        self.show_state("paused")

    def show_no_match(self):
        self.show_state("no_match")

    @property
    def playing_state(self) -> bool:
        return self._play_state

    def show_seek(self, seconds: int):
        self._last_seek = seconds
        self.show_state("seek")

    def handle_touch(self) -> dict[str, Any] | None:
        if self._pending_touch is None:
            return None
        event = self._pending_touch
        self._pending_touch = None
        return self._interpret_touch(event)

    def _interpret_touch(self, event: TouchEvent) -> dict[str, Any]:
        if event.kind == "play_pause":
            return {"action": "pause" if self.playing_state else "play"}
        if event.kind == "back":
            return {"action": "back"}
        if event.kind == "forward":
            return {"action": "forward"}
        return {"action": "play"}
