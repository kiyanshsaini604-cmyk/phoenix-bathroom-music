import asyncio
import logging
import re
from dataclasses import dataclass
from typing import Any

LOG = logging.getLogger("phoenix.voice")


@dataclass
class Command:
    action: str
    text: str
    artist: str | None = None
    title: str | None = None
    seconds: int | None = None
    confidence: float = 0.0


class Pipeline:
    def __init__(self, config: dict):
        self.config = config
        self.wake_phrase = config.get("wake_phrase", "hey phoenix").lower()
        self.default_seek_seconds = int(config.get("default_seek_seconds", 15))
        self._wake_detected = False
        self._recognizer_lock = asyncio.Lock()

    @property
    def wake_detected(self) -> bool:
        return self._wake_detected

    async def capture_and_recognize(self) -> Command | None:
        async with self._recognizer_lock:
            LOG.info("Capturing command after wake")
            text = "play last nite by the strokes"
            return self.parse(text)

    def parse(self, text: str) -> Command | None:
        cleaned = self.normalize(text)
        if not cleaned:
            return None
        lowered = cleaned.lower()
        if lowered.startswith("play "):
            return self._parse_play(lowered[5:])
        if lowered in ("pause", "stop"):
            return Command(action="pause", text=cleaned, confidence=1.0)
        if lowered in ("play",):
            return Command(action="play", text=cleaned, confidence=1.0)
        if lowered.startswith("back "):
            return self._parse_seek(lowered, "back")
        if lowered.startswith("forward "):
            return self._parse_seek(lowered, "forward")
        if lowered in ("back", "rewind"):
            return Command(action="back", text=cleaned, confidence=1.0)
        if lowered in ("forward", "skip", "next"):
            return Command(action="forward", text=cleaned, confidence=1.0)
        LOG.info("Unrecognized command: %s", cleaned)
        return None

    def _parse_play(self, after_play: str) -> Command:
        artist, title, _tail = self._split_artist_title(after_play)
        return Command(
            action="play_song_by_artist_title",
            text=after_play,
            artist=artist or None,
            title=title or None,
            confidence=0.9,
        )

    def _parse_seek(self, text: str, direction: str) -> Command:
        matched = re.search(r"(\d+)\s*(second|sec|s|minute|min)?", text)
        if matched:
            value = int(matched.group(1))
            unit = (matched.group(2) or "").lower()
            if unit.startswith("min"):
                value = value * 60
            return Command(action=direction, text=text, seconds=value, confidence=0.95)
        return Command(action=direction, text=text, seconds=None, confidence=0.9)

    def _split_artist_title(self, text: str) -> tuple[str, str, str]:
        by_index = text.lower().find(" by ")
        if by_index == -1:
            by_index = text.lower().find(" - ")
        if by_index == -1:
            by_index = text.lower().find(",")
        if by_index == -1:
            return "", text.strip(), ""
        artist = text[:by_index].strip()
        tail = text[by_index + 4:].strip() if text[by_index : by_index + 3].lower() == "by " else text[by_index + 3:].strip()
        return artist, tail, ""

    def normalize(self, text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r"[.,!?;:]+", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()
