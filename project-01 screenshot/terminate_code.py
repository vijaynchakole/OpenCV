# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:02:45 2020

@author: hp
"""

import cv2
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
    
    

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()    
    

    
