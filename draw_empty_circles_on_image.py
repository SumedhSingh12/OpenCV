import cv2
import numpy as np

def draw_circle(event, x,y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 45,(0,0,255),5,)
img = cv2.imread('DATA/dog_backpack.jpg')
cv2.namedWindow(winname = 'dog')
cv2.setMouseCallback('dog',draw_circle)

while(True):
    cv2.imshow('dog',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break;
cv2.destroyAllWindows()