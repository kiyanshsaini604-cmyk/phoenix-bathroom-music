import asyncio

import phoenix.music


def test_client_stores_server_config(music_client):
    assert music_client.server_url is not None
    assert music_client.user is not None


def test_authenticate_returns_token(music_client):
    token = music_client.authenticate()
    assert token is not None


def test_search_query_is_normalized(music_client):
    query = music_client.normalize_query("  The  Strokes  ,  Last  Nite  ")
    assert query == "the strokes last nite"


def test_search_accepts_artist_and_title(music_client):
    result = asyncio.run(music_client.search(artist="Arcade Fire", title="Wake Up"))
    assert isinstance(result, list)
    assert len(result) > 0


def test_search_returns_empty_list_for_unknown_query(music_client):
    result = asyncio.run(music_client.search(artist="Unknown", title="Unknown Song"))
    assert result == []


def test_play_track_returns_track_reference(music_client):
    track = asyncio.run(music_client.play_track("dummy-track-id"))
    assert track is not None
    assert track["id"] == "dummy-track-id"


def test_play_toggle_changes_playing_state(music_client):
    assert music_client.playing is False
    asyncio.run(music_client.play_track("dummy-track-id"))
    assert music_client.playing is True


def test_pause_changes_playing_state(music_client):
    asyncio.run(music_client.play_track("dummy-track-id"))
    assert music_client.playing is True
    asyncio.run(music_client.pause())
    assert music_client.playing is False


def test_resume_changes_playing_state(music_client):
    asyncio.run(music_client.play_track("dummy-track-id"))
    asyncio.run(music_client.pause())
    asyncio.run(music_client.resume())
    assert music_client.playing is True


def test_seek_uses_given_seconds(music_client):
    asyncio.run(music_client.play_track("dummy-track-id"))
    result = asyncio.run(music_client.seek(20))
    assert result == 20


def test_default_seek_defaults_to_fifteen_seconds(music_client):
    asyncio.run(music_client.play_track("dummy-track-id"))
    result = asyncio.run(music_client.seek())
    assert result == 15


def test_status_returns_current_state(music_client):
    status = music_client.status
    assert "playing" in status
    assert "track" in status
