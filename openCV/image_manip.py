import os
import cv2

img = cv2.imread(os.path.join('.', 'images', 'dogs.jpeg'))
cv2.imshow('Image', img)
cv2.waitKey(0)