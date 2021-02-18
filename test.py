import time

from pynput import *
from pynput.mouse import Controller, Button

from init import *

mouse = Controller()
#-------------------------


temp = 1
while (True):
    time.sleep(1)
    if check_screen("interface") == "menu_bar_half":
        print("Game screen loaded")
        break
    print("Waiting for game screen to load! (" + str(temp) + ")")
    temp = temp + 1
    if temp == 20:
        exit("Can't find game screen!")