import os

from moves import *

# settings
mouse = Controller()


# ------------------------------------------------------
def start(iterations):
    for i in range(iterations):

        # wait for character selection frame
        misc_wait_for_frame("iface_menu_bar_half")
        print("asd")

start(20000)
