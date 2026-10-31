import phoenix.voice


def test_normalize_lowercases_and_strips_punctuation():
    pipeline = phoenix.voice.Pipeline({"wake_phrase": "hey phoenix"})
    assert pipeline.normalize("  The  Strokes,  Last  Nite!  ") == "the strokes last nite"


def test_parse_play_command():
    pipeline = phoenix.voice.Pipeline({"wake_phrase": "hey phoenix"})
    cmd = pipeline.parse("play last nite by the strokes")
    assert cmd is not None
    assert cmd.action == "play_song_by_artist_title"
    assert cmd.artist == "last nite"
    assert cmd.title == "the strokes"


def test_parse_pause_command():
    pipeline = phoenix.voice.Pipeline({"wake_phrase": "hey phoenix"})
    cmd = pipeline.parse("pause")
    assert cmd is not None
    assert cmd.action == "pause"


def test_parse_back_with_seconds():
    pipeline = phoenix.voice.Pipeline({"wake_phrase": "hey phoenix"})
    cmd = pipeline.parse("back 10 seconds")
    assert cmd is not None
    assert cmd.action == "back"
    assert cmd.seconds == 10


def test_parse_forward_without_seconds():
    pipeline = phoenix.voice.Pipeline({"wake_phrase": "hey phoenix"})
    cmd = pipeline.parse("forward")
    assert cmd is not None
    assert cmd.action == "forward"
    assert cmd.seconds is None


def test_parse_forward_with_minutes():
    pipeline = phoenix.voice.Pipeline({"wake_phrase": "hey phoenix"})
    cmd = pipeline.parse("forward 2 minutes")
    assert cmd is not None
    assert cmd.action == "forward"
    assert cmd.seconds == 120


def test_parse_unrecognized_returns_none():
    pipeline = phoenix.voice.Pipeline({"wake_phrase": "hey phoenix"})
    cmd = pipeline.parse("enable the nebula")
    assert cmd is None
