# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:04:48 2020

@author: Vijay Narsing Chakole

Topic : knn digits

"""

import cv2
import numpy as np 
import os
import matplotlib.pyplot as plt

os.chdir("C:\\Users\\hp\\Desktop\\practicals_ml\\OpenCV\\Project - 05 Hand_Written_digits_recognition\\")

digits = cv2.imread("digits.png", cv2.IMREAD_GRAYSCALE )
test_digits = cv2.imread("test_digits.png", cv2.IMREAD_GRAYSCALE)


digits.shape



def show_img_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    # img_RGB = color_img[:, :, ::-1]

    # ax = plt.subplot(2, 2, pos)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    
    
show_img_with_matplotlib(cv2.cvtColor(digits, cv2.COLOR_GRAY2RGB), "")

show_img_with_matplotlib(cv2.cvtColor(test_digits, cv2.COLOR_GRAY2RGB), "")

test_digits = np.vsplit(test_digits, 50)

# test digits
test_cells = []

for d in test_digits :
    d = d.flatten()
    test_cells.append(d)
    
test_cells = np.array(test_cells, dtype =np.float32)
rows = np.vsplit(digits, 50)


#putiing all the elements in the array(50x50=2500 digits)
cells = []

for row in rows :
    element = np.hsplit(row, 50)
    for i in element :
        i = i.flatten()
        cells.append(i)
        
    
# convert to numpy array
cells = np.array(cells, dtype = np.float32)

# made to specify the first 250 are zeros and
# the next 250 are ones and so on
k = np.arange(10)
cells_label = np.repeat(k, 250)


# loading KNN(K Nearest Neighbour Algo)

knn = cv2.ml.KNearest_create()
knn.train(cells, cv2.ml.ROW_SAMPLE, cells_label)


ret, result, neighbours, dist = knn.findNearest(test_cells, k = 3)



# K value is then nbr of nearest neighbours that we need to find
# K can be any 'odd' value

print(result)