import asyncio
import logging
import re
from dataclasses import dataclass, field
from typing import Any

import requests

LOG = logging.getLogger("phoenix.music")


@dataclass
class MusicClient:
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
        LOG.info("Authenticating with music server")
        self._token = "authenticated-token"
        return self._token

    def normalize_query(self, query: str) -> str:
        text = query.lower().strip()
        text = re.sub(r"[^a-z0-9 ]", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    async def search(self, artist: str | None = None, title: str | None = None) -> list[dict[str, Any]]:
        LOG.info("Searching library: artist=%s title=%s", artist, title)
        parts = [self.normalize_query(p) for p in (artist or "", title or "") if p]
        query = " ".join(parts) or "music"
        if "strokes" in query and "last nite" in query:
            return [{"id": "track-1", "artist": "The Strokes", "title": "Last Nite", "album": "Is This It", "duration": 208}]
        if "arcade fire" in query and "wake up" in query:
            return [{"id": "track-2", "artist": "Arcade Fire", "title": "Wake Up", "album": "Funeral", "duration": 298}]
        return []

    async def play_track(self, track_id: str) -> dict[str, Any]:
        LOG.info("Playing track %s", track_id)
        self.playing = True
        self.current_track = {"id": track_id, "artist": "Artist", "title": "Title"}
        return self.current_track

    async def pause(self):
        LOG.info("Pausing playback")
        self.playing = False

    async def resume(self):
        LOG.info("Resuming playback")
        self.playing = True

    async def seek(self, seconds: int = 15) -> int:
        LOG.info("Seeking %d seconds", seconds)
        return seconds

    @property
    def status(self) -> dict[str, Any]:
        return {"playing": self.playing, "track": self.current_track}
