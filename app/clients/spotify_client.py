# spotify_client.py

class SpotifyClient:

    def __init__(self, spotify_links):
        self.links = spotify_links


    def generate_uris(self):
        """Converts the urls in links to the correct URI format required
        for the embedded players."""

        result = {
    		'track': [],
    		'artist': [],
    		'album': [],
    		'playlist': []
        }

        for url in self.links:
            for link_type in result:
                if link_type in url:
                    result[link_type].append(self.convert_to_uri(link_type, url))

        return result


    def convert_to_uri(self, link_type, url):
        """Converts a Spotify URL into a URI."""
        unique_id = url.split('/')[-1]
        return 'spotify%3{link_type}%3{unique_id}'.format(
            link_type=link_type, unique_id=unique_id
        )
