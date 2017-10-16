import cv2
import numpy as np
#读取图像
img = cv2.imread('testimg.jpg')
#显示图像
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Applying Grayscale filter to image 作用Grayscale（灰度）过滤器到图像上
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#保存过滤过的图像到新文件中
cv2.imwrite('graytest.jpg',gray)