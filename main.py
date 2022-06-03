import cv2
import numpy as np
from cv2 import Mat

DENSITY_1 = "@#W$9876543210?!abc;:+=-,._                    "
DENSITY_2 = '      .:-i|=+%O#@'

def convert_to_bw(image: Mat):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def get_character_index (pixel, DENSITY):

    raw_position = np.floor(pixel / len(DENSITY))
    remainder = pixel % len(DENSITY)

    charIndex = raw_position + 1 if (remainder < len(DENSITY) / 2) else raw_position
    return int(charIndex)

def image_to_ascii(image, DENSITY):
    ascii_image = ""
    for row in image:
        for pixel in row:
            char = DENSITY[get_character_index(pixel, DENSITY)]
            ascii_image += char
        ascii_image += "\n"
    return ascii_image

def resize_image(img: Mat, scale: int) -> Mat or None:
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


test_image = cv2.imread("./assets/test-image.jpg")

resized = resize_image(test_image, 25)

grey_image = convert_to_bw(resized)

ascii_image = image_to_ascii(grey_image, DENSITY_2)

with open(f"test-ascii-.txt", "w") as file:
    file.write(ascii_image)