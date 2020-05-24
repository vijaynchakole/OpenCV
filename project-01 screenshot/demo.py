# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:15:40 2020

@author: Vijay Narsing Chakole

"""

# import important libraries
import cv2
import numpy as np
import pyautogui
import schedule
import time 
import datetime
from pynput import keyboard

number = 1
flag = 0
character = "z"
def screenshot():
    global number 
    
    print("inside screenshot Current time : ", datetime.datetime.now())
    image = pyautogui.screenshot()
    
    # since pyautogui takes as PIL(pillow) and in RGB format 
    # we need to convert it into numpy array and BGR format
    # so that we can save it to the disk
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    #writting image to the disk
    cv2.imwrite("screenshot_"+str(number)+".png", image)
    
    number = number + 1
    

def screenshot_schedule(): 
    global flag
    schedule.every(2).seconds.do(screenshot)
    while True :
        schedule.run_pending()
        time.sleep(1)
        if flag == 1 :
            break


    
def on_press(key):
    try:
        global character
        print('alphanumeric key {0} pressed'.format(
            key.char))
        character  = "a"
        screenshot_schedule()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))





def on_release(key):
    global flag
    print('{0} released'.format(key)) 
    if key == keyboard.Key.esc:
        flag = 1
        # stop listener
        return False
    
    
def main():
    global flag 
    global character
    
    with keyboard.Listener(on_press=on_press,on_release = on_release) as listener:
        listener.join()
    # human image synthesis technology project
    # deep learning + fake = deep fake
    # frankenstein monster
    
    print("inside Main Current time : ", datetime.datetime.now())
    
    # take screenshot after every 15 seconds
    schedule.every(2).seconds.do(screenshot)
    
    # take screenshot after every 1 minute
    schedule.every(1).minutes.do(screenshot)
    
    # take screenshot after every 1 hour
    schedule.every(1).hour.do(screenshot)
    
    # take screenshot after every sunday
    schedule.every().sunday.do(screenshot)
    
    # take screenshot after everyday at 12pm (afternoon) 
    schedule.every().day.at("12:00").do(screenshot)
    
    if character == "a" :
        while True :
            schedule.run_pending()
            time.sleep(1)    
            if flag == 1 :
                break
    

  

        
if __name__ == "__main__":
    main()
