import os
import cv2
from utils import ( resize_image, 
    convert_to_bw, 
    get_character_index, 
    image_to_ascii
)

DENSITY_1 = "@#W$9876543210?!abc;:+=-,._                    "
DENSITY_2 = '      .:-i|=+%O#@'

cam = cv2.VideoCapture(0)

while True:

    ret, image = cam.read()

    if not ret: break

    grey_image = convert_to_bw(image)

    resized = resize_image(grey_image, 5)

    os.system("cls")

    print(image_to_ascii(resized, DENSITY_2))

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()