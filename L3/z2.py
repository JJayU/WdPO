import cv2
import numpy as np

def empty_callback(emm):
    pass

img = cv2.imread('obraz.png', 0)

cv2.namedWindow('Rozmiar')
cv2.createTrackbar('RozmiarBar', 'Rozmiar', 1, 20, empty_callback)

while True:
    
    rozmiar = cv2.getTrackbarPos('RozmiarBar', 'Rozmiar')
    
    if rozmiar % 2 != 1:
        rozmiar = rozmiar - 1
    
    if rozmiar < 3:
        rozmiar = 3
    
    ret, gotowe = cv2.threshold(img,126,255,cv2.THRESH_BINARY)
    kernel = np.ones((rozmiar,rozmiar), np.uint8)
    erozja = cv2.erode(gotowe, kernel, iterations=1)
    dylatacja = cv2.dilate(gotowe, kernel, iterations=1)
    
    zamkniecie = cv2.morphologyEx(gotowe, cv2.MORPH_CLOSE, kernel)
    otwarcie = cv2.morphologyEx(gotowe, cv2.MORPH_OPEN, kernel)
    
    cv2.imshow('Oryginal', img)
    cv2.imshow('Sprogowane', gotowe)
    cv2.imshow('Erode', erozja)
    cv2.imshow('Dilate', dylatacja)
    cv2.imshow('Zamkniecie', zamkniecie)
    cv2.imshow('Otwarcie', otwarcie)
    
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()