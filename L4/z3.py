import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img_kol = cv.imread('gory.jpg')
img_czb = cv.imread('gory.jpg', 0)

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img_kol],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

while(1):
    cv.imshow('Kolorowy', img_kol)
    cv.imshow('CzarnoBialy', img_czb)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()