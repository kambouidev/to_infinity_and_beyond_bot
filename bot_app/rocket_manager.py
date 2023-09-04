import json, math
from .video_list_service import video_list
from .tuplas import image_data

class RocketManager:
    """
    This class manages rocket-related operations such as getting rocket images and calculating next images.
    """

    #def get_rocket_image() -> RocketInfo:
    def get_rocket_image():
        """
        Retrieves information about a rocket image for starting a challenge.
        """
        meta_data = video_list.get_meta_data_video()
        bisection_frame = RocketManager.bisection_calculate_frame(meta_data.frames, 0)
        url_image = video_list.get_url_image_video_by_frame(meta_data.url, bisection_frame)
        return image_data(
            image_url=url_image,
            max_frame=meta_data.frames,
            min_frame=0,
            step=0,
            current_frame=bisection_frame,
            url=meta_data.url,
            is_rocket_launched='',
            max_steps=round(math.log2(meta_data.frames))
        )

    def get_next_image(json_img_data) -> image_data:
        """
        Calculates and returns the next image data based on the current image data and rocket launch status.
        """
        #data_dict = json.loads(json_img_data)
        if isinstance(json_img_data, image_data):
            img_data = json_img_data
        else:
            img_data = image_data(json_img_data)
        
        new_data_img = img_data._replace()

        if img_data.is_rocket_launched == 'no':
            new_data_img = new_data_img._replace(
                min_frame=img_data.current_frame,
                max_frame=img_data.max_frame,
                current_frame=RocketManager.bisection_calculate_frame(img_data.max_frame, img_data.current_frame) + img_data.current_frame
            )
        else:
            new_data_img = new_data_img._replace(
                min_frame=img_data.min_frame,
                max_frame=img_data.current_frame,
                current_frame=RocketManager.bisection_calculate_frame(img_data.current_frame, img_data.min_frame) + img_data.min_frame
            )
        
        new_data_img = new_data_img._replace(
            image_url=video_list.get_url_image_video_by_frame(new_data_img.url, new_data_img.current_frame),
            step=new_data_img.step + 1,
            is_rocket_launched=''
        )
        
        return new_data_img        

    def bisection_calculate_frame(max_val: int, min_val: int) -> int:
        """
        Calculates the midpoint frame value using the bisection method.
        """
        return round((max_val - min_val) / 2)

