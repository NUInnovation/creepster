# youtube_client.py

class YoutubeClient:

    def __init__(self, youtube_links):
        self.links = youtube_links


    def generate_uris(self):
        """Converts the urls in links to the correct URI format required
        for the embedded players."""

        uris = []
        for url in self.links:
            identifier = url.split('?v=')[1]
            uri = 'http://www.youtube.com/embed/' + identifier
            uris.append(uri)

        return uris
