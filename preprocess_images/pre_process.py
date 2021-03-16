import numpy as np
import glob
from PIL import Image
import time
import cv2


# dimensions used to resize images
X_DIM, Y_DIM = 448, 448

# percentage of image to crop off top
CROP_PER = 0.08


def main():
    # compute and output runtime of script
    before_time = time.time()
    crop_images()
    resize_images()
    after_time = time.time()
    time_elapsed = after_time - before_time
    print(time_elapsed)


def crop_images():
    # crop and save all files in the folder
    for file in glob.iglob('COVIDxCT-2A/COVIDx_CT_2A_images/*.png'):
        img = Image.open(file)
        f_name = img.filename
        data = np.asarray(img)
        x, y, a, b = 0, CROP_PER * data.shape[0], data.shape[1], data.shape[0]
        dim = (x, y, a, b)
        img = Image.fromarray(data)
        img = img.crop(dim)
        img.save(f_name)


def resize_images():
    # resize all files in folder to 448 x 448
    for file in glob.iglob('COVIDxCT-2A/COVIDx_CT_2A_images/*.png'):
        img = Image.open(file)
        f_name = img.filename
        data = np.asarray(img)
        resized = cv2.resize(data, (X_DIM, Y_DIM))
        img = Image.fromarray(resized)
        img.save(f_name)


main()
