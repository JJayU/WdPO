import cv2 as cv
import numpy as np
import math

def empty_callback(emm):
    pass

zdjecie = cv.imread('obraz.jpg', 0)

cv.namedWindow('Progi')
cv.createTrackbar('Prog1Bar', 'Progi', 50, 255, empty_callback)
cv.createTrackbar('Prog2Bar', 'Progi', 100, 255, empty_callback)

while True:         
    
    prog1 = cv.getTrackbarPos('Prog1Bar', 'Progi')
    prog2 = cv.getTrackbarPos('Prog2Bar', 'Progi')
    
    wynik = cv.Canny(zdjecie, prog1, prog2)
    
    cv.imshow('Wynik', wynik)
    
    key_code = cv.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break

cv.destroyAllWindows()

# do projektu przydatna funkcja cv.inRange do progowania obrazu !!!!
# cv.findCountours do wyszukiwania konturów obiektów