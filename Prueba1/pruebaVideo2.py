import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while(1):
    _, frame = cam.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('camara', frame)
    cv2.imshow('gris', gris)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()