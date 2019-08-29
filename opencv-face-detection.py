import inline
import numpy as np
import cv2
import matplotlib.pyplot as plt


def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


haar_cascade_face = cv2.CascadeClassifier('Haar-Cascade-Files/haarcascade_frontalface_default.xml')

# Loading the image to be tested
test_image = cv2.imread('Images/baby.png')

faces = haar_cascade_face.detectMultiScale(test_image, scaleFactor=1.2, minNeighbors=5)
print('Faces found: ', len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(test_image, (x, y), (x + w, y + h), (250, 110, 241), 4)

plt.imshow(convertToRGB(test_image))
if plt.waitforbuttonpress(0) & 0xFF == 27:
    plt.close()
