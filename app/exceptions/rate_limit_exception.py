# rate_limit_exception.py

class RateLimitException(Exception):
    """Exception thrown when an API rate limit has been exceeded."""

    def __init__(self, platform):
        self.platform = platform

    def __str__(self):
        return repr('Rate limit exceeded for {platform} API!'.format(platform=self.platform))
