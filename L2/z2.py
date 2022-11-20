import cv2
import numpy as np

def empty_callback(emm):
    pass

img = cv2.imread('obraz.png', 0)

cv2.namedWindow('okno')
cv2.createTrackbar('Prog', 'okno', 127, 255, empty_callback)
cv2.createTrackbar('Metoda', 'okno', 0, 4, empty_callback)

while True:
    
    prog = cv2.getTrackbarPos('Prog', 'okno')
    metoda = cv2.getTrackbarPos('Metoda', 'okno')
    
    if metoda == 0:
        ret, gotowe = cv2.threshold(img,prog,255,cv2.THRESH_BINARY)
    elif metoda == 1:
        ret, gotowe = cv2.threshold(img,prog,255,cv2.THRESH_BINARY_INV)
    elif metoda == 2:
        ret, gotowe = cv2.threshold(img,prog,255,cv2.THRESH_TOZERO)
    elif metoda == 3:
        ret, gotowe = cv2.threshold(img,prog,255,cv2.THRESH_TOZERO_INV)
    elif metoda == 4:
        ret, gotowe = cv2.threshold(img,prog,255,cv2.THRESH_TRUNC)
    
    cv2.imshow('okno', gotowe)
    
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()