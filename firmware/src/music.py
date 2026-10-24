"""Subsonic-compatible music client glue sketch for Phoenix."""

CLIENT_USER = "user"
CLIENT_PASS = "changeme"
SERVER_URL = "http://music.local:4040"


def search(artist=None, title=None):
    """Search the library for likely candidates."""


def play_track(track_id):
    """Start playback for a matched track."""


def pause():
    """Pause playback."""


def resume():
    """Resume playback."""


def seek(seconds):
    """Seek relative to current position."""
