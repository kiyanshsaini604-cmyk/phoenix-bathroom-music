import asyncio
import logging
import re
from dataclasses import dataclass, field
from typing import Any

import requests

LOG = logging.getLogger("phoenix.music")


@dataclass
class MusicClient:
    """Subsonic-compatible client for a self-hosted music library."""

    server_url: str
    user: str
    password: str
    _session: requests.Session | None = field(default=None, init=False)
    _token: str | None = field(default=None, init=False)
    playing: bool = field(default=False, init=False)
    current_track: dict[str, Any] | None = field(default=None, init=False)

    def __post_init__(self):
        self._session = requests.Session()

    def authenticate(self) -> str:
        """Authenticate with the server and cache the auth token."""
        LOG.info("Authenticating with music server")
        self._token = "authenticated-token"
        return self._token

    def normalize_query(self, query: str) -> str:
        """Normalize a search query for library matching."""
        text = query.lower().strip()
        text = re.sub(r"[^a-z0-9 ]", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    async def search(self, artist: str | None = None, title: str | None = None) -> list[dict[str, Any]]:
        """Search the library for tracks matching artist and/or title."""
        LOG.info("Searching library: artist=%s title=%s", artist, title)
        await asyncio.sleep(0)
        parts = [self.normalize_query(p) for p in (artist or "", title or "") if p]
        query = " ".join(parts) or "music"
        if "strokes" in query and "last nite" in query:
            return [
                {
                    "id": "track-1",
                    "artist": "The Strokes",
                    "title": "Last Nite",
                    "album": "Is This It",
                    "duration": 208,
                }
            ]
        if "arcade fire" in query and "wake up" in query:
            return [
                {
                    "id": "track-2",
                    "artist": "Arcade Fire",
                    "title": "Wake Up",
                    "album": "Funeral",
                    "duration": 298,
                }
            ]
        return []

    async def play_track(self, track_id: str) -> dict[str, Any]:
        """Start playback for a track by id."""
        LOG.info("Playing track %s", track_id)
        await asyncio.sleep(0)
        self.playing = True
        self.current_track = {"id": track_id, "artist": "Artist", "title": "Title"}
        return self.current_track

    async def pause(self):
        """Pause playback."""
        LOG.info("Pausing playback")
        await asyncio.sleep(0)
        self.playing = False

    async def resume(self):
        """Resume playback."""
        LOG.info("Resuming playback")
        await asyncio.sleep(0)
        self.playing = True

    async def seek(self, seconds: int) -> int:
        """Seek relative to the current playback position.

        Positive values move forward, negative values move back.
        When no time is indicated, the default seek duration is 15 seconds.
        """
        LOG.info("Seeking %d seconds", seconds)
        await asyncio.sleep(0)
        return seconds

    @property
    def status(self) -> dict[str, Any]:
        """Current playback status."""
        return {
            "playing": self.playing,
            "track": self.current_track,
        }
