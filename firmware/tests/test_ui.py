import phoenix.ui


def test_screen_starts_in_idle():
    screen = phoenix.ui.Screen()
    assert screen.state == "idle"


def test_show_playing_sets_state():
    screen = phoenix.ui.Screen()
    screen.show_playing({"id": "t1", "artist": "A", "title": "B"})
    assert screen.state == "playing"
    assert screen._last_track == {"id": "t1", "artist": "A", "title": "B"}


def test_show_paused_sets_state():
    screen = phoenix.ui.Screen()
    screen.show_paused()
    assert screen.state == "paused"


def test_show_no_match_sets_state():
    screen = phoenix.ui.Screen()
    screen.show_no_match()
    assert screen.state == "no_match"


def test_show_seek_sets_state_and_value():
    screen = phoenix.ui.Screen()
    screen.show_seek(-10)
    assert screen.state == "seek"
    assert screen._last_seek == -10


def test_handle_touch_returns_command_when_pending():
    screen = phoenix.ui.Screen()
    screen._pending_touch = phoenix.ui.TouchEvent(kind="play_pause")
    cmd = screen.handle_touch()
    assert cmd is not None
    assert cmd["action"] == "pause"


def test_handle_touch_clears_pending_after_use():
    screen = phoenix.ui.Screen()
    screen._pending_touch = phoenix.ui.TouchEvent(kind="play_pause")
    screen.handle_touch()
    assert screen._pending_touch is None


def test_handle_touch_returns_none_when_idle():
    screen = phoenix.ui.Screen()
    assert screen.handle_touch() is None
