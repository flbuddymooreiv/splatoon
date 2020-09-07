#!/usr/bin/env python3

import cv2
import numpy as np

img = cv2.imread('doc.png', cv2.IMREAD_COLOR)
#img = cv2.medianBlur(img,5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

gray_blurred = gray #cv2.blur(gray, (3,3))

cv2.imwrite('docgrayblurred.png', gray_blurred)

#detected_circles = cv2.HoughCircles(
#    gray_blurred, cv2.HOUGH_GRADIENT, dp = 1, 
#    minDist = 100, param1 = 50, param2 = 30, 
#    minRadius = 20, maxRadius = 150)

detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 
    dp=1, minDist=500, param1=100, param2=2, 
    minRadius=5, maxRadius=50)

#circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                            param1=50,param2=30,minRadius=30,maxRadius=150)

#circles = np.uint16(np.around(circles))

if detected_circles.any():
    detected_circles = np.uint16(np.around(detected_circles))
    for i in detected_circles[0,:]:
        # draw the outer circle
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite('doccircles.png', img)
