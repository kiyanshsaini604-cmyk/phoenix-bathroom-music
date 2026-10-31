"""
Phoenix device-side orchestrator.

This is the main service layer for the Phoenix bathroom voice music device.
It ties together startup, audio, voice, music client, screen, and touch input.
"""

import asyncio
import signal
import logging

from phoenix.config import load
from phoenix.audio import AudioManager
from phoenix.voice import Pipeline
from phoenix.music import MusicClient
from phoenix.ui import Screen

LOG = logging.getLogger("phoenix")


class Phoenix:
    def __init__(self, config_path="config/device.json"):
        self.config = load(config_path)
        self.server_cfg = self.config["server"]
        self.voice_cfg = self.config["voice"]
        self.client = MusicClient(self.server_cfg["url"], self.server_cfg["user"], self.server_cfg["password"])
        self.pipeline = Pipeline(self.voice_cfg)
        self.audio = AudioManager()
        self.screen = Screen()
        self.running = False

    async def start(self):
        LOG.info("Phoenix starting up")
        await self.audio.start()
        self.client.authenticate()
        self.screen.show_state("idle")
        self.running = True

    async def run(self):
        await self.start()
        try:
            while self.running:
                await self._tick()
                await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            await self.shutdown()

    async def _tick(self):
        touched = self.screen.handle_touch()
        if touched:
            await self._handle_touch(touched)
            return
        if self.pipeline.wake_detected:
            await self._handle_wake()

    async def _handle_wake(self):
        self.screen.show_state("listening")
        command = await self.pipeline.capture_and_recognize()
        self.screen.show_state("recognized")
        if not command:
            self.screen.show_no_match()
            return
        await self._handle_command(command)

    async def _handle_touch(self, command):
        await self._handle_command(command)

    async def _handle_command(self, command):
        action = command["action"]
        if action == "play":
            await self.client.resume()
            self.screen.show_playing(self.client.current_track)
        elif action == "pause":
            await self.client.pause()
            self.screen.show_paused()
        elif action == "back":
            seconds = command.get("seconds") or self.voice_cfg["default_seek_seconds"]
            await self.client.seek(-int(seconds))
            self.screen.show_seek(-int(seconds))
        elif action == "forward":
            seconds = command.get("seconds") or self.voice_cfg["default_seek_seconds"]
            await self.client.seek(int(seconds))
            self.screen.show_seek(int(seconds))
        elif action == "play_song_by_artist_title":
            track = await self._match_and_play(command["artist"], command["title"])
            if track:
                self.screen.show_playing(track)
            else:
                self.screen.show_no_match()

    async def _match_and_play(self, artist, title):
        results = await self.client.search(artist=artist, title=title)
        if not results:
            return None
        best = results[0]
        return await self.client.play_track(best["id"])

    async def shutdown(self):
        LOG.info("Phoenix shutting down")
        await self.audio.stop()
        self.running = False


async def main():
    phoenix = Phoenix()
    loop = asyncio.get_running_loop()
    stop = lambda: setattr(phoenix, "running", False)
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, stop)
        except NotImplementedError:
            signal.signal(sig, lambda *_: stop())
    await phoenix.run()
    LOG.info("Phoenix shutting down")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
