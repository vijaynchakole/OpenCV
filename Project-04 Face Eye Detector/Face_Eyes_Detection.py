# -*- coding: utf-8 -*-
"""
Created on Wed May  6 02:26:39 2020

@author: Vijay Narsing Chakole

Topic : Face Eyes Detection

"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

os.chdir("C:\\Users\\hp\\Desktop\\practicals_ml\\OpenCV\\Project-04 Face Eye Detector\\")

# haarcascade_eye.xml

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


#image = cv2.imread("vijay_image.png", cv2.IMREAD_COLOR)
image = cv2.imread("vijay_face_image.jpg", cv2.IMREAD_COLOR)
image = cv2.imread("childhood.jpg", cv2.IMREAD_COLOR)


def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


show_with_matplotlib(image, "Vijay")

while True :
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image)
    
    for (fx, fy, fw, fh) in faces :
        cv2.putText(image, 'face', (fx, fy), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 255, 255), 2, cv2.LINE_AA )
        cv2.rectangle(image, (fx, fy), (fx+fw,fy+fh), (255,0,0), 2)
        
        roi_gray = gray_image[fy : fy+fh, fx:fx+fw]
        roi_color = image[fy:fy+fh, fx:fx+fw]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes :
            cv2.putText(roi_color, 'eye', (ex,ey), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 255, 255), 2, cv2.LINE_AA)
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255), 2)
            
            
    cv2.imshow('Face and eyes Detection', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cv2.destroyAllWindows()    