import cv2
from cffi.backend_ctypes import xrange
from matplotlib import pyplot as plt
import glob


def main():
    mask_img()
    mask_all_imgs()
    
# compute and plot an image with different thresholds
def mask_img():
    # load image
    img = cv2.imread("CP_2429_2890_0063.png")

    # convert image to gray-scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # global thresholding
    glob_thresh, glob_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Otsu's thresholding
    otsu_noise_thresh, otsu_noise_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # filter with 5x5 gaussian kernel to reduce noise
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # apply Otsu's thresholding with Gaussian filtered noise reduction
    otsu_threshold, otsu_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # store images and corresponding titles in lists
    images = [img, 0, glob_img,
              img, 0, otsu_noise_img,
              img, 0, otsu_img]

    titles = ['Original Image', 'Histogram', 'Global Thresholding',
              'Original Image', 'Histogram', "Otsu's Thresholding",
              'Gaussian Filtered Image', 'Histogram', "Otsu's Thresholding"]

    # plot results
    for i in xrange(3):
        plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
        plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
        plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
        plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
    plt.show()
    
# apply Otsu's Thresholding to images and save
def mask_all_imgs():
    for file in glob.iglob('images/*.png'):
        # load image
        img = cv2.imread(file)

        # create image masks file name
        f_name = img.filename
        length = len(f_name)
        length -= 4
        f_new_name = f_name[0:length]
        f_new_name += "mask.png"

        # convert image to gray-scale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # filter with 5x5 gaussian kernel to reduce noise
        img = cv2.GaussianBlur(img, (5, 5), 0)

        # apply Otsu's thresholding with Gaussian filtered noise reduction
        otsu_threshold, otsu_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        otsu_img.save(f_new_name)

main()

