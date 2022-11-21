import numpy as np
import cv2 as cv

pozycje = np.zeros((4,2), np.float32)
numer_punktu = 0
pozycje2 = np.float32([[0,0],[500,0],[0,500],[500,500]])

def obsluga_myszki(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        przesuniecie = 0
        while przesuniecie < 4 and pozycje[numer_punktu+przesuniecie, 0] != 0 and pozycje[numer_punktu+przesuniecie, 1] != 0:
            przesuniecie = przesuniecie + 1
        if przesuniecie < 4:
            pozycje[numer_punktu + przesuniecie] = (x,y)
        if przesuniecie == 3:
            przeksztalcenie()


img = cv.imread('road(2).jpg')
dst = np.zeros((1000, 1000), np.uint8)
cv.namedWindow('okno')
cv.setMouseCallback('okno', obsluga_myszki)

def przeksztalcenie():
    M = cv.getPerspectiveTransform(pozycje, pozycje2)
    dst = cv.warpPerspective(img, M, (500, 500))
    cv.imshow('okno2', dst)

while(1):
    cv.imshow('okno', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()