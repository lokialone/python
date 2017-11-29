import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# blue = np.uint8([[[0,0,255]]])
# hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
# print(hsv_blue)
while(1):

#     # Take each frame
    _, frame = cap.read()

#     # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    

    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])

    lower_red = np.array([20, 20, 20])  
    upper_red = np.array([200, 200, 200])

# Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    
    mask = mask_blue + mask_green + mask_red
#     # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask_blue)

    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()