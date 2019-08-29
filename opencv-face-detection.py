import inline
import numpy as np
import cv2
import matplotlib.pyplot as plt


def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


haar_cascade_face = cv2.CascadeClassifier('Haar-Cascade-Files/haarcascade_frontalface_default.xml')


# Loading the image to be tested
test_image = cv2.imread('Images/baby.png')
test_image = convertToRGB(test_image)

# Converting to grayscale
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Displaying the grayscale image
plt.imshow(test_image, cmap='gray')
if plt.waitforbuttonpress(0) & 0xFF == 27:
    plt.close()
