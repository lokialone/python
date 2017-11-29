import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('frame.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
res = cv2.bitwise_and(img, img, mask= mask_blue)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()