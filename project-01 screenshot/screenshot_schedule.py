# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:27:17 2020

@author: Vijay Narsing Chakole

"""
# import important libraries
import cv2
import numpy as np
import pyautogui
import schedule
import time 
import datetime

number = 1

def screenshot():
    global number 
    
    print("inside screenshot Current time : ", datetime.datetime.now())
    image = pyautogui.screenshot()
    
    # since pyautogui takes as PIL(pillow) and in RGB format 
    # we need to convert it into numpy array and BGR format
    # so that we can save it to the disk
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    #writting image to the disk
    cv2.imwrite("test_"+str(number)+".png", image)
    
    number = number + 1
    
def main():
    
    # human image synthesis technology project
    # deep learning + fake = deep fake
    # frankenstein monster
    
    print("inside Main Current time : ", datetime.datetime.now())
    
    # take screenshot after every 15 seconds
    schedule.every(15).seconds.do(screenshot)
    
    # take screenshot after every 1 minute
    schedule.every(1).minutes.do(screenshot)
    
    # take screenshot after every 1 hour
    schedule.every(1).hour.do(screenshot)
    
    # take screenshot after every sunday
    schedule.every().sunday.do(screenshot)
    
    # take screenshot after everyday at 12pm (afternoon) 
    schedule.every().day.at("12:00").do(screenshot)
    
    
    
    
    
    while True :
        schedule.run_pending()
        time.sleep(1)
        
        
if __name__ == "__main__":
    main()