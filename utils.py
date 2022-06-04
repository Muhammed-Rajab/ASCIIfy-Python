import cv2
import numpy as np
from cv2 import Mat

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
            index = get_character_index(pixel, DENSITY)
            # print(index, pixel, len(DENSITY),  pixel % len(DENSITY), pixel / len(DENSITY))
            char = DENSITY[index]
            ascii_image += char
        ascii_image += "\n"
    return ascii_image

def resize_image(img: Mat, scale: int) -> Mat or None:
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)