from ctypes import windll, Structure, c_long, byref
import keyboard as keyboard
import win32api
import win32gui
import win32ui
import numpy as np
from PIL import ImageGrab
import cv2
from ctypes import windll, Structure, c_long, byref
from ctypes.wintypes import POINT
import PIL

from positions import calculate_obj_in_view_position

global starting_cords, click, found_coords


# 1025x850
class Mouse:
    """
        Checking mouse position
    """

    def queryMousePosition(self):
        point = POINT()
        windll.user32.GetCursorPos(byref(point))
        return point.x, point.y


# Gathering some info
while True:
    try:
        # if keyboard.is_pressed('p'):  # if key 'q' is pressed
        print('Got starting position')
        # cords = Mouse().queryMousePosition()
        starting_cords = [176, 315]
        calculate_obj_in_view_position(starting_cords[0], starting_cords[1])
        break
    except:
        print("Error while setting proper mouse settings , retrying...")
