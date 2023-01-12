from PIL import Image, ImageDraw, ImageFont


def make_facet_img(facet: int):
    img = Image.new('RGBA', (300, 300), "grey")
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((25, 25, 275, 275), radius=15, fill='black')
    draw.rounded_rectangle((50, 50, 250, 250), radius=15, fill="grey")
    font = ImageFont.truetype("Alice-Regular.ttf", 120)
    draw.text((150, 150), text=f"{facet}", anchor="mm", fill="black",font=font)
    return img
