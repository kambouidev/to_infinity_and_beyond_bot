import requests
from .tuplas import meta_data

class VideoList:
    """
    This class handles video-related operations such as fetching metadata and constructing URLs.
    """
    def __init__(self):
        self.URL_API = 'https://framex-dev.wadrid.net/api/video/?format'

    def get_meta_data_video(self) -> meta_data:
        """
        Retrieves metadata about a video from the API.
        """
        response = requests.get(self.URL_API)
        data = response.json()[0]
        
        return meta_data(
            frames = data['frames'],
            url = data['url']
        )

    def get_url_image_video_by_frame(self, url: str, frame_number: int) -> str:
        """
        Constructs the URL for an image of the video based on the frame number.
        """
        return f"{self.query_params_take_out(url)}frame/{frame_number}/"

    def query_params_take_out(self, url: str) -> str:
        """
        Removes query parameters from a URL.
        """
        is_query_param_exist = '?' in url
        return url.split('?')[0] if is_query_param_exist else url

video_list = VideoList()
