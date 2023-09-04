from typing import NamedTuple, Tuple

class meta_data(NamedTuple):
    #name: str
    #width: int
    #height: int
    frames: int
    #frame_rate: Tuple[int, int]
    url: str
    #first_frame: str
    #last_frame: str

class image_data(NamedTuple):
    image_url: str
    max_frame: int
    min_frame: int
    step: int
    max_steps: int
    current_frame: int
    url: str
    is_rocket_launched: str
