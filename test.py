import time

from pynput import *
from pynput.mouse import Controller, Button

from init import *
from moves import check_if_frame_exists, main_choose_char_slot, main_click_play, interface_eq_find_item, \
    interface_eq_use_item, game_get_to_main_menu, misc_wait_for_frame, game_reset

mouse = Controller()
# -------------------------


game_reset()
