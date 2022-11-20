from turtle import goto, shape
import cv2
import numpy as np
import datetime

img = cv2.imread('obraz.png', 0)

while True:
    
    max_y = img.shape[0]
    max_x = img.shape[1]
    
    gotowe = np.zeros((max_y, max_x), np.uint8)

    t1 = datetime.datetime.now()
    
    for y in range(1, max_y-1):
        for x in range(1, max_x-1):
            
            suma = 0
            
            for y_2 in range(y-1, y+2):
                for x_2 in range(x-1, x+2):
                    suma = suma + img[y_2, x_2]
            
            srednia = suma / 9
            
            gotowe[y,x] = srednia
            
    t2 = datetime.datetime.now()
    
    t_diff = t2 - t1

    print('For:')
    print(t_diff)
    
    ######################3
    
    t1 = datetime.datetime.now()
    
    gotowe2 = cv2.blur(img, (3,3))
    
    t2 = datetime.datetime.now()
    
    t_diff = t2 - t1
    
    print('Blur:')
    print(t_diff)
    
    
    
    cv2.imshow('For', gotowe)
    cv2.imshow('Blur', gotowe2)
    cv2.imshow('Oryginal', img)
    
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()