from PIL import Image, ImageDraw


def make_template() -> None:
    im = Image.new("RGBA", (300, 300), "grey")
    draw = ImageDraw.Draw(im)
    draw.rounded_rectangle((25, 25, 275, 275),
                           radius=30,
                           outline="black",
                           fill="grey",
                           width=25)
    im.show()


make_template()

