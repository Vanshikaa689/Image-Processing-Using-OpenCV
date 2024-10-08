import imutils
import cv2
import numpy as np

i=cv2.imread(r'C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\IMAGE TRANSFORMS\dark.jpeg')
blurImg = cv2.blur(i,(10, 10)) 
cv2.imshow('Original image',i)
  
cv2.waitKey(0)
cv2.imshow('blurred image',blurImg)
  
cv2.waitKey(0)
