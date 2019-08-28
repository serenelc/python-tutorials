import inline as inline
import numpy as np
import cv2
import matplotlib.pyplot as plt

img_raw = cv2.imread('Images/mandrill-colour.png')
print(f"The type of the opened image is: {type(img_raw)}")
print(f"The shape of the image is: {img_raw.shape}")

# OpenCV reads images in the form of BGR, whereas matplotlib reads RGB
img_rgb = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.waitforbuttonpress(0)

plt.imshow(img_raw)
plt.waitforbuttonpress(0)

while True:
    cv2.imshow('mandrill', img_raw)

    if cv2.waitKey(1) & 0xFF == 27:
        # waitKey() Waits for specified milliseconds for any keyboard event.
        # If you press any key in that time, the program continues
        # 27 is the esc keyboard key
        break

cv2.destroyAllWindows()

# cv2.imwrite('final_image.png',img)

