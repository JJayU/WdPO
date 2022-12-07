import cv2 as cv
import numpy as np
import math

def empty_callback(emm):
    pass

zdjecie = cv.imread('shapes.jpg', 0)
zdjecie = cv.medianBlur(zdjecie, 5)
czdjecie = cv.cvtColor(zdjecie, cv.COLOR_GRAY2BGR)
0
circles = cv.HoughCircles(zdjecie,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(czdjecie,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(czdjecie,(i[0],i[1]),2,(0,0,255),3)

while True:         
    
    cv.imshow('Wynik', czdjecie)
    
    key_code = cv.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break

cv.destroyAllWindows()

# do projektu przydatna funkcja cv.inRange do progowania obrazu !!!!
# cv.findCountours do wyszukiwania konturów obiektów