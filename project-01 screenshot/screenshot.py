# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 07:31:06 2020

@author: Vijay Narsing Chakole


"""

import numpy as np
import cv2
import pyautogui





# take  screenshot using pyautogui
image = pyautogui.screenshot()
    


# since pyautogui takes as PIL(pillow) and in RGB format 
# we need to convert it into numpy array and BGR format 
# so that we can save it to the  disk
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# writing image to the disk
cv2.imwrite("test.png",image)



    