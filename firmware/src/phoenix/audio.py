import asyncio
import logging
from contextlib import asynccontextmanager

import pyaudio

LOG = logging.getLogger("phoenix.audio")


class AudioManager:
    """Manages microphone capture and speaker playback for the device."""

    def __init__(self):
        self._pyaudio = None
        self._capture_stream = None
        self._playback_stream = None
        self._capturing = False
        self._playing = False

    async def start(self):
        LOG.info("Starting audio subsystem")
        self._pyaudio = pyaudio.PyAudio()
        await asyncio.sleep(0)

    async def stop(self):
        LOG.info("Stopping audio subsystem")
        await self.capture_stop()
        await self.playback_stop()
        if self._pyaudio is not None:
            self._pyaudio.terminate()
            self._pyaudio = None

    # Capture API

    async def capture_start(self):
        if self._capturing:
            return
        LOG.info("Starting microphone capture")
        self._capturing = True
        await asyncio.sleep(0)

    async def capture_stop(self):
        if not self._capturing:
            return
        LOG.info("Stopping microphone capture")
        self._capturing = False
        await asyncio.sleep(0)

    async def capture_frame(self) -> bytes:
        if not self._capturing:
            raise RuntimeError("capture not started")
        await asyncio.sleep(0)
        return b"\x00" * 1024

    # Playback API

    async def playback_start(self):
        if self._playing:
            return
        LOG.info("Starting speaker playback")
        self._playing = True
        await asyncio.sleep(0)

    async def playback_stop(self):
        if not self._playing:
            return
        LOG.info("Stopping speaker playback")
        self._playing = False
        await asyncio.sleep(0)

    async def play_frame(self, frame: bytes):
        if not self._playing:
            raise RuntimeError("playback not started")
        await asyncio.sleep(0)
