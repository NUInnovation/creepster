# no_twitter_acccount_exception.py

class NoTwitterAccountException(Exception):
    """Exception thrown when no twitter account is found for the
    given name"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)