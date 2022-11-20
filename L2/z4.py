import cv2
import numpy as np

def empty_callback(emm):
    pass

img = cv2.imread('obraz.png')
logo = cv2.imread('logo.png')

cv2.namedWindow('okno')

while True:
    logoscaled = cv2.resize(logo, (472, 438))
    polaczenie = cv2.addWeighted(img, 0.8, logo, 0.2, 0)
    
    cv2.imshow('wynik', polaczenie)
    
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)  # MUSI BYĆ KIEDY JEST imshow()!!!
    if key_code == 27:
        # escape key pressed
        break


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()