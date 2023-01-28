from io import BytesIO
from random import randint
from PIL.Image import Image as ImageClass
from PIL import Image, ImageDraw, ImageFont


def _roll_dice(dice: int) -> int:
    return randint(1, dice)


def _from_image_to_bytes(img: ImageClass) -> bytes:
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="PNG")
    return img_byte_arr.getvalue()


def _make_image(number: int) -> ImageClass: 
    img = Image.open("src/images/template.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("src/fonts/Alice-Regular.ttf", 120)
    draw.text((150, 150), text=f"{number}",
              anchor="mm", fill="black", font=font)
    return img


def print_number(dice: int) -> bytes:
    number = _roll_dice(dice)
    img = _make_image(number)
    return _from_image_to_bytes(img)

