import os

from moves import *

# settings
mouse = Controller()


# ------------------------------------------------------
def start(iterations):
    for i in range(iterations):

        # wait for character selection frame
        misc_wait_for_frame_and_click_on_it("minigame_play_button", 2)
        print("asd")

start(20000)
