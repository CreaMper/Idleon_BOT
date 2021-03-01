from moves import *

# settings
mouse = Controller()
char_slot = 4



while True:
    if game_reset():
        break

# wait for character selection frame
misc_wait_for_frame("main_menu_play_button")
time.sleep(2)  # loading offset

# click on proper character slot
main_choose_char_slot(char_slot)

# wait for confirmation that character was choose
misc_wait_for_frame("main_menu_main_stats")
main_click_play()
