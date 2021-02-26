import time

from pynput import *
from pynput.mouse import Controller, Button

from init import *
from moves import check_if_frame_exists, main_choose_char_slot, main_click_play, interface_eq_find_item, \
    interface_eq_use_item, game_get_to_main_menu, misc_wait_for_frame

mouse = Controller()
#-------------------------


# sprawdz czy jest klucz w eq , zapisz jego kordy

key = interface_eq_find_item("amarok_key")
print(key)
# uzyj przedmiotu
if key != 0:
    # użycie klucza
    interface_eq_use_item(key)
    # zapisywanie postępów
    game_get_to_main_menu()
