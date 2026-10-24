class PhoenixError(Exception):
    """Base exception for Phoenix device errors."""


class ConfigError(PhoenixError):
    """Raised when the device configuration is invalid."""


class ServerError(PhoenixError):
    """Raised when the music server request failed."""


class RecognitionError(PhoenixError):
    """Raised when speech recognition produced unusable output."""


class PlaybackError(PhoenixError):
    """Raised when audio playback could not be started or controlled."""


class NoMatchError(PhoenixError):
    """Raised when no library match was found for a request."""
