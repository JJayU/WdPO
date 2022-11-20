import cv2
import numpy as np

img = cv2.imread("lenna_salt_and_pepper.bmp")

def empty_callback(emm):
    pass

cv2.namedWindow('Rozmiar')
cv2.createTrackbar('RozmiarBar', 'Rozmiar', 1, 20, empty_callback)

while True:
    rozmiar = cv2.getTrackbarPos('RozmiarBar', 'Rozmiar')
    
    if rozmiar % 2 != 1:
        rozmiar = rozmiar - 1
    
    if rozmiar < 3:
        rozmiar = 3
    
    cv2.imshow('Original', img)
    med = cv2.medianBlur(img, rozmiar)
    cv2.imshow('Median Blur', med)
    gaus = cv2.GaussianBlur(img, (rozmiar, rozmiar), 0)
    cv2.imshow('Gaussian Blur', gaus)
    ave = cv2.blur(img, (rozmiar, rozmiar))
    cv2.imshow('Average Blur', ave)
    
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()