from pros import pros_vision_function
from time import sleep
import cv2
import numpy as np
from PIL import Image

i = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

input_img = cv2.imread('C:/Users/hp/downloads/trekar.jpg')
gray_input = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
inputimg = cv2.imwrite('gray_screen.jpg', gray_input)
    
# Resize smoothly down to 16x16 pixels
Img = Image.open('gray_screen.jpg')
pixel_img_16 = Img.resize((16,16),resample=Image.BILINEAR)
pixel_img_16.save('test_16_test.jpg')
    
    # equalize the histogram of the Y channel    
pixel = cv2.imread('test_16_test.jpg')
img_yuv = cv2.cvtColor(pixel, cv2.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    
    # convert the YUV image back to RGB format
img_equalized = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
cv2.imwrite('C:/Users/hp/Documents/test/Assets/Resources/trekar.png', img_equalized)
