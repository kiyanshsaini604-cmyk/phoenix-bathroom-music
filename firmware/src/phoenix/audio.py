import asyncio
import logging

LOG = logging.getLogger("phoenix.audio")


class AudioManager:
    def __init__(self):
        self._capturing = False
        self._playing = False

    async def start(self):
        LOG.info("Starting audio subsystem")

    async def stop(self):
        LOG.info("Stopping audio subsystem")
        await self.capture_stop()
        await self.playback_stop()

    async def capture_start(self):
        if self._capturing:
            return
        LOG.info("Starting microphone capture")
        self._capturing = True

    async def capture_stop(self):
        if not self._capturing:
            return
        LOG.info("Stopping microphone capture")
        self._capturing = False

    async def capture_frame(self) -> bytes:
        if not self._capturing:
            raise RuntimeError("capture not started")
        return b"\x00" * 1024

    async def playback_start(self):
        if self._playing:
            return
        LOG.info("Starting speaker playback")
        self._playing = True

    async def playback_stop(self):
        if not self._playing:
            return
        LOG.info("Stopping speaker playback")
        self._playing = False

    async def play_frame(self, frame: bytes):
        if not self._playing:
            raise RuntimeError("playback not started")
