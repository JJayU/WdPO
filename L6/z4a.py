import cv2 as cv
import numpy as np
import math

def empty_callback(emm):
    pass

zdjecie = cv.imread('shapes.jpg', cv.COLOR_BGR2GRAY)
edges = cv.Canny(zdjecie, 50, 150)
linie = cv.HoughLines(edges, 1, np.pi/180, 120)

for line in linie:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 10000*(-b))
    y1 = int(y0 + 10000*(a))
    x2 = int(x0 - 10000*(-b))
    y2 = int(y0 - 10000*(a))
    cv.line(zdjecie,(x1,y1),(x2,y2),(0,0,255),2)
    print(line)

while True:         
    
    cv.imshow('Wynik', zdjecie)
    
    key_code = cv.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break

cv.destroyAllWindows()

# do projektu przydatna funkcja cv.inRange do progowania obrazu !!!!
# cv.findCountours do wyszukiwania konturów obiektów