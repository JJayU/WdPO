import cv2 as cv
import numpy as np
import math

def empty_callback(emm):
    pass

zdjecie = cv.imread('drone_ship.jpg', 0)

# Detekcja okregow
zdjecie_rozmyte = cv.medianBlur(zdjecie, 5)
czdjecie = cv.cvtColor(zdjecie_rozmyte, cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(zdjecie,cv.HOUGH_GRADIENT,1,20,param1=100,param2=70,minRadius=40,maxRadius=150)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(czdjecie,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(czdjecie,(i[0],i[1]),2,(0,0,255),3)
    
# Detekcja linii
edges = cv.Canny(zdjecie, 50, 150)
linie = cv.HoughLinesP(edges, 1, np.pi/180, 110, minLineLength=70, maxLineGap=50)
wynik_linie = zdjecie

for line in linie:
    x1,y1,x2,y2 = line[0]
    cv.line(wynik_linie,(x1,y1),(x2,y2),(0,255,0),2)

while True:         
    
    cv.imshow('Wynik_okregi', czdjecie)
    cv.imshow('Wynik_linie', wynik_linie)
    
    print(np.amax(zdjecie))
    
    key_code = cv.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break

cv.destroyAllWindows()

# do projektu przydatna funkcja cv.inRange do progowania obrazu !!!!
# cv.findCountours do wyszukiwania konturów obiektów