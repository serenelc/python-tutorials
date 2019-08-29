import inline
import numpy as np
import cv2
import matplotlib.pyplot as plt


def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def detect_faces(cascade, img, scaleFactor=1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = img.copy()

    # convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    faces = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
    print('Faces found: ', len(faces))

    for (x, y, w, h) in faces:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (250, 110, 241), 5)

    return image_copy


haar_cascade_face = cv2.CascadeClassifier('Haar-Cascade-Files/haarcascade_frontalface_default.xml')

test_image = cv2.imread('Images/group-of-people.jpg')
new_image = detect_faces(haar_cascade_face, test_image)

plt.imshow(convertToRGB(new_image))
if plt.waitforbuttonpress(0) & 0xFF == 27:
    plt.close()
