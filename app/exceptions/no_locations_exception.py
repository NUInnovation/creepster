# no_locations_exception.py

class NoLocationsException(Exception):
    """Exception raised when no locations found in user media."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
