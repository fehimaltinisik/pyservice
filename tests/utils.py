from PIL import Image


def save_image(image_name, image_bytes):
    image = Image.open(image_bytes)
    image.save(f"{image_name}.png")
