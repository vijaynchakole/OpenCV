# -*- coding: utf-8 -*-
"""
Created on Tue May  5 06:49:35 2020

@author: Vijay Narsing Chakole

Body Detection 

"""

import cv2
import os
import matplotlib.pyplot as plt

os.chdir("C:\\Users\\hp\\Desktop\\practicals_ml\\OpenCV\\Project-03 Body Detection\\")
#sample1.jpg

detector = cv2.CascadeClassifier("haarcascade_fullbody.xml")
image = cv2.imread("sample1.jpg", cv2.IMREAD_COLOR)
#image = cv2.imread("download.jpg", cv2.IMREAD_COLOR)

def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


show_with_matplotlib(image, "")
i = 2
ID = "out_sample" + str(i)


while True :
    body = detector.detectMultiScale(image, 1.1, 4)
    
    for(x,y,w,h) in body :
        cv2.rectangle(image,(x,y),(x+w,x+h),(255,0,0),2)
        
        # saving captured body in the directory 
        cv2.imwrite(ID+".jpg", image[y:y+h, x:x+w])
        # showing image with a rectangle surrounding the body
        cv2.imshow("frame", image )

    
    # press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    
cv2.destroyAllWindows()
