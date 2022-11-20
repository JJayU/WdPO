from turtle import goto, shape
import cv2
import numpy as np

img = cv2.imread('obraz.png', 0)

while True:
    
    max_y = img.shape[0]
    max_x = img.shape[1]
    
    gotowe = np.zeros((max_y, max_x), np.uint8)
    
    for y in range(0, max_y):
        for x in range(0, max_x):
            if x % 3 == 0:
                gotowe[y,x] = 255
            else:
                gotowe[y,x] = img[y,x]
    
    cv2.imshow('Gotowe', gotowe)
    cv2.imshow('Oryginal', img)
    
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()