import time

from pynput import *
from pynput.mouse import Controller, Button

from init import *

mouse = Controller()

# sprawdz czy amarok is ded
if check_screen("amarok") == "amarok_dead":
    print("Amarok is ded! Siara , Amarok jest ded!")
else:
    exit("Why is he still alive...")