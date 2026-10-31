import asyncio

import phoenix.audio


def test_audio_manager_starts_without_error():
    mgr = phoenix.audio.AudioManager()
    asyncio.run(mgr.start())
    assert mgr._capturing is False


def test_audio_manager_capture_state():
    mgr = phoenix.audio.AudioManager()
    assert mgr._capturing is False


def test_audio_manager_playback_state():
    mgr = phoenix.audio.AudioManager()
    assert mgr._playing is False
