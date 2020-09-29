### https://github.com/yogeshwaran-shanmuganathan ###

import cv2
import numpy as np

# number of downsampling steps
num_down = 2
# number of bilateral filtering steps
num_bilateral = 7

img_rgb = cv2.imread("test_img.jpg")
print(img_rgb.shape) #gives the dimensions of the image

# resizing to get optimal results after unsampling is done
img_rgb=cv2.resize(img_rgb,(800,800))

# downsample using Gaussian Pyramid
img_color = img_rgb
for _ in range(num_down):
    img_color = cv2.pyrDown(img_color)

# apply small bilateral filters repeatedly instead of applying one large filter
for _ in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

# upsample image to original size
for _ in range(num_down):
    img_color = cv2.pyrUp(img_color)

img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                 blockSize=9, C=2)

# convert black to color, bitwise AND with color image
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color,img_edge)
stack=np.hstack([img_rgb,img_cartoon])
cv2.imshow('Cartoonizer',stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
