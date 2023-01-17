from io import BytesIO
from random import randint
from PIL import Image

def roll_dice(dice: int) -> int:
    return randint(1, dice)

def from_image_to_bytes(img: Image):
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="JPEG")
    return img_byte_arr.getvalue()

    
