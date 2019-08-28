import inline as inline
import numpy as np
import cv2
import matplotlib.pyplot as plt

# creates a black image
black_img = np.zeros(shape=(512, 512, 3), dtype = np.int16)

# draws a red line from (0,0) to (511, 511) with a thickness of 5 onto black_img
line_red = cv2.line(black_img, (0, 0), (511, 511), (255, 0, 0), 5)

# draws a green line from (511, 0) to (0, 511) with a thickness of 3 onto line_red
line_green = cv2.line(line_red, (511, 0), (0, 511), (0, 255, 0), 3)

# draws a blue rectangle with top left corner (180, 180) and bottom right corner (300, 300)
rectangle = cv2.rectangle(line_green, (180, 180), (330, 330), (0, 0, 255), 5)

# -1 is a filled in circle. center (251, 251) with radius 10
circle = cv2.circle(rectangle, (254, 254), 20, (235, 52, 186), -1)

plt.imshow(circle)
if plt.waitforbuttonpress(0) & 0xFF == 27:
    plt.close()

