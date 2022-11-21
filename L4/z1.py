import numpy as np
import cv2 as cv

def obsluga_myszki(event, x, y, flags, param):
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 50, 255, 1)
    elif event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x-50,y-50), (x+50, y+50), 255)

img = np.zeros((1000, 1000), np.uint8)
cv.namedWindow('okno')
cv.setMouseCallback('okno', obsluga_myszki)

while(1):
    cv.imshow('okno', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()