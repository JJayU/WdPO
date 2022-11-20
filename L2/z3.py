import cv2
import numpy as np

def empty_callback(emm):
    pass

img = cv2.imread('qr.jpg')

cv2.namedWindow('okno')

while True:
    
    obraz1 = cv2.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LINEAR)
    obraz2 = cv2.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv2.INTER_NEAREST)
    obraz3 = cv2.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv2.INTER_AREA)
    obraz4 = cv2.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LANCZOS4)
    
    cv2.imshow('INTER_LINEAR', obraz1)
    cv2.imshow('INTER_NEAREST', obraz2)
    cv2.imshow('INTER_AREA', obraz3)
    cv2.imshow('INTER_LANCZOS4', obraz4)
    
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()