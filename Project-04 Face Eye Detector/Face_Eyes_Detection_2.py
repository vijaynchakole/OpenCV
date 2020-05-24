# -*- coding: utf-8 -*-
"""
Created on Wed May  6 03:42:34 2020

@author: hp
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

images = []
images_path = "C:\\Users\\hp\\Desktop\\practicals_ml\\OpenCV\\test_images"
for image_file in os.listdir(images_path):
    # there are total 7 images
    print(image_file)
    
    
    image = cv2.imread(os.path.join(images_path,image_file), cv2.IMREAD_COLOR)
    
    images.append(image)






from random import randint

fig, ax = plt.subplots(2, 4)
#fig.subplots_adjust(0,0,3,3)
num = 0
for i in range(0,2,1):
    for j in range(0,4,1):
        #random_num = randint(0, len(train_images))
        ax[i,j].show_with_matplotlib(images[num], "")
        #ax[i,j].set_title(get_classlabel(train_labels[random_num])) #important line , I was stuck here for long time
        ax[i,j].axis('off')
        num = num + 1
        
    





images[0]
# haarcascade_eye.xml

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# images[1] gives perfect result
image = cv2.imread(images[1], cv2.IMREAD_COLOR)
#image = cv2.imread("vijay_face_image.jpg", cv2.IMREAD_COLOR)
#image = cv2.imread("childhood.jpg", cv2.IMREAD_COLOR)
images[1].shape
image.shape
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    #img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(title)
    plt.show()


show_with_matplotlib(images[1], "Vijay")


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image)

while True :
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