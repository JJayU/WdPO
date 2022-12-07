import cv2 as cv
import numpy as np
import math

def empty_callback(emm):
    pass

zdjecie = cv.imread('shapes.jpg', cv.COLOR_BGR2GRAY)
edges = cv.Canny(zdjecie, 50, 150)
linie = cv.HoughLinesP(edges, 1, np.pi/180, 70, minLineLength=30, maxLineGap=20)

for line in linie:
    x1,y1,x2,y2 = line[0]
    cv.line(zdjecie,(x1,y1),(x2,y2),(0,255,0),2)

while True:         
    
    cv.imshow('Wynik', zdjecie)
    
    key_code = cv.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break

cv.destroyAllWindows()

# do projektu przydatna funkcja cv.inRange do progowania obrazu !!!!
# cv.findCountours do wyszukiwania konturów obiektów