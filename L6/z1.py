import cv2 as cv
import numpy as np
import math

zdjecie = cv.imread('obraz.jpg', 0)

filtr_x = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])/3
filtr_y = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])/3

wynik_x = abs(cv.filter2D(zdjecie, cv.CV_32F, filtr_x))/255.0
wynik_y = abs(cv.filter2D(zdjecie, cv.CV_32F, filtr_y))/255.0

wynik_modul = np.zeros(np.shape(zdjecie), float)

#print(np.shape(zdjecie))

for y in range(0, np.shape(zdjecie)[0]):
    for x in range(0, np.shape(zdjecie)[1]):
        wynik_modul[y,x] = math.sqrt(pow(wynik_x[y,x],2)+pow(wynik_y[y,x],2))#*math.atan2(x,y)
        #print(wynik_modul[y,x])

while True:
    
    #cv.imshow('Oryginal', zdjecie)
    
    #cv.imshow('x', wynik_x)
    #cv.imshow('y', wynik_y)            
    
    cv.imshow('Wynik', wynik_modul)
    
    key_code = cv.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break

print(np.max(wynik_modul))
cv.destroyAllWindows()

# do projektu przydatna funkcja cv.inRange do progowania obrazu !!!!
# cv.findCountours do wyszukiwania konturów obiektów