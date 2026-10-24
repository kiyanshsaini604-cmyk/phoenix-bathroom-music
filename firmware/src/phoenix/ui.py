import asyncio
import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any

LOG = logging.getLogger("phoenix.ui")


class DeviceState(Enum):
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
    """Screen visuals and touch input for the device.

    The screen is both the display and the main touch surface, so this
    module owns state feedback and input interpretation.
    """

    def __init__(self):
        self.state: DeviceState | str = "idle"
        self._pending_touch: TouchEvent | None = None
        self._last_track: dict[str, Any] | None = None
        self._last_seek: int = 0

    def show_state(self, state: str):
        """Set the visible device state."""
        LOG.info("Showing state: %s", state)
        self.state = state

    def show_idle(self):
        """Show the calm idle screen."""
        self.show_state("idle")

    def show_listening(self):
        """Show the listening indicator."""
        self.show_state("listening")

    def show_recognized(self):
        """Show the recognized-command state."""
        self.show_state("recognized")

    def show_playing(self, track: dict[str, Any] | None = None):
        """Show the now-playing screen."""
        self._last_track = track
        self.show_state("playing")

    def show_paused(self):
        """Show the paused state."""
        self.show_state("paused")

    def show_no_match(self):
        """Show the no-match / unknown command state."""
        self.show_state("no_match")

    def show_seek(self, seconds: int):
        """Show seek feedback."""
        self._last_seek = seconds
        self.show_state("seek")

    def handle_touch(self) -> dict[str, Any] | None:
        """Return a touch command if the user touched the screen."""
        if self._pending_touch is None:
            return None
        event = self._pending_touch
        self._pending_touch = None
        return self._interpret_touch(event)

    def _interpret_touch(self, event: TouchEvent) -> dict[str, Any]:
        if event.kind == "play_pause":
            return {"action": "pause" if self.state == "playing" else "play"}
        if event.kind == "back":
            return {"action": "back"}
        if event.kind == "forward":
            return {"action": "forward"}
        return {"action": "play"}
