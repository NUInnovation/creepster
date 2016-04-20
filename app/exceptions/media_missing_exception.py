# media_missing_exception.py

class MediaMissingException(Exception):
    """Exception thrown when no user media is provided by API.
    This usually means that the user has a private account."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
