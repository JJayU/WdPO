import numpy as np
import cv2 as cv

pozycje = np.zeros((4,2), np.float32)
numer_punktu = 0
pozycje2 = np.float32([[0,0],[460,0],[0,290],[460,290]])

def obsluga_myszki(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        przesuniecie = 0
        while przesuniecie < 4 and pozycje[numer_punktu+przesuniecie, 0] != 0 and pozycje[numer_punktu+przesuniecie, 1] != 0:
            przesuniecie = przesuniecie + 1
        if przesuniecie < 4:
            pozycje[numer_punktu + przesuniecie] = (x,y)
        if przesuniecie == 3:
            przeksztalcenie()


img = cv.imread('gallery.png')
img2 = cv.imread('pug.png')
dst = np.zeros((1000, 1000), np.uint8)
cv.namedWindow('okno')
cv.setMouseCallback('okno', obsluga_myszki)

def przeksztalcenie():
    M = cv.getPerspectiveTransform(pozycje2, pozycje)
    dst = cv.warpPerspective(img2, M, (1200, 801))

    rows, cols, channels = img2.shape
    roi = img[0:rows, 0:cols]

    img2gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img2gray, 0, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)

    img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

    cv.imshow('dst', img)

    dst2 = cv.addWeighted(img, 0.5, dst, 0.5, 0)

    cv.imshow('okno2', dst2)

while(1):
    cv.imshow('okno', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()