import time
from pynput.mouse import Controller, Button
from positions import *
from init import *
from resources import check_screen
from positions import *
mouse = Controller()


def check_if_frame_exists(target, desc):
    """
    :param target: what element in that category we are looking for
    :param desc: description that will be printed after function ends
    """
    if check_screen(target) == target:
        print(desc + " Found!")
        return True
    else:
        exit(desc + " Not Found!")


def check_if_frame_exists_optional(target, desc):
    """
    :param target: what element in that category we are looking for
    :param desc: description that will be printed after function ends
    :param return: returns true if  frame was found
    """
    if check_screen(target) == target:
        print(desc + "Found!")
        return True
    else:
        return False


def main_choose_char_slot(choosen_char):
    """
    :param choosen_char:  choosen char
    """
    if choosen_char == 1:
        mouse.position = (char1[0], char1[1])
    elif choosen_char == 2:
        mouse.position = (char2[0], char2[1])
    elif choosen_char == 3:
        mouse.position = (char3[0], char3[1])
    elif choosen_char == 4:
        mouse.position = (char4[0], char4[1])
    elif choosen_char == 5:
        mouse.position = (char5[0], char5[1])
    time.sleep(0.5)
    mouse.click(Button.left)
    time.sleep(0.5)
    print("Choosed slot" + str(choosen_char))


def main_click_play():
    mouse.position = (login_start[0], login_start[1])
    time.sleep(0.5)
    mouse.click(Button.left)
    time.sleep(0.5)


def mouse_click(pos, button, delay):
    """
    :param pos: target position , one dimensional array that sould be taken from init
    :param button: which button have to be clicked 0 - left , 1 right
    :param delay:  delay after click
    """
    mouse.position = (pos[0], pos[1])
    if button == 0:
        mouse.click(Button.left)
    else:
        mouse.click(Button.right)
    time.sleep(delay)


def mouse_click_double(pos, button, delay):
    """
    :param pos: target position , one dimensional array that sould be taken from init
    :param button: which button have to be clicked 0 - left , 1 right
    :param delay:  delay after click
    """
    mouse.position = (pos[0], pos[1])
    if button == 0:
        mouse.click(Button.left)
    else:
        mouse.click(Button.right)
    time.sleep(0.5)
    if button == 0:
        mouse.click(Button.left)
    else:
        mouse.click(Button.right)
    time.sleep(delay)


def mouse_loot_swing(target_left, target_right):
    """
    :param target_left:  target start position , one dimensional array that sould be taken from init
    :param target_right:  target end position , one dimensional array that sould be taken from init
    :param delay:  delay bettwen mouse clicks in loop
    """
    mouse.position = (target_left[0], target_left[1])
    iteration = round(abs(target_left[0] - target_right[0]) / 10)

    mouse.press(Button.left)
    for i in range(iteration):
        mouse.position = (target_left[0] + (i * 10), target_left[1])
        time.sleep(0.05)
    mouse.release(Button.left)


def interface_eq_find_item(item, bags):
    """
    :param item: item that function is looking for, check names in init
    :param bags: bag slots
    :return: returns cords of mouse if successfully, returns False if not
    """
    mouse.position = (items[0], items[1])
    mouse.click(Button.left)
    time.sleep(1)

    mouse.position = (eq_slotbar1[0], eq_slotbar1[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen(item)[0] == item:
        print(item + "found at bag bar 1")
        cords = check_screen(item)[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]
    if bags == 1:
        return False

    mouse.position = (eq_slotbar2[0], eq_slotbar2[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen(item)[0] == item:
        print(item + "Found at bag bar 2")
        cords = check_screen(item)[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]
    if bags == 2:
        return False

    mouse.position = (eq_slotbar3[0], eq_slotbar3[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen(item)[0] == item:
        print(item + "Found at bag bar 3")
        cords = check_screen(item)[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]
    if bags == 3:
        return False

    mouse.position = (eq_slotbar4[0], eq_slotbar4[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen(item)[0] == item:
        print(item + "Found at bag bar 4")
        cords = check_screen(item)[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]
    if bags == 4:
        return False

    mouse.position = (eq_slotbar5[0], eq_slotbar5[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen(item)[0] == item:
        print(item + "Found at bag bar 5")
        cords = check_screen(item)[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]

    return False


def interface_eq_use_item(cords):
    """
    :param cords: cordinates of an item
    """
    mouse.position = (cords[0], cords[1])
    mouse.press(Button.left)
    time.sleep(1)
    mouse.release(Button.left)


def game_get_to_main_menu():
    mouse.position = (menu[0], menu[1])
    time.sleep(0.5)
    mouse.click(Button.left)

    while True:
        if check_screen("iface_menu_swap_players") == "iface_menu_swap_players":
            break
        time.sleep(0.5)

    mouse.position = (menu_swap_players[0], menu_swap_players[1])
    time.sleep(0.5)
    mouse.click(Button.left)

    while True:
        if check_screen("iface_menu_swap_players_player_menu") == "iface_menu_swap_players_player_menu":
            break
        time.sleep(0.5)

    mouse.position = (menu_swap_players_player_menu[0], menu_swap_players_player_menu[1])
    time.sleep(0.5)
    mouse.click(Button.left)

    while True:
        if check_screen("main_menu_play_button") == "main_menu_play_button":
            break
        time.sleep(0.5)


def misc_wait_for_frame(target):
    """
    :param target: what to looking for
    :return:
    """
    tries = 0
    while True:
        print("Looking for " + str(target))
        tries = tries + 1
        if check_screen(target) == target:
            return True
        time.sleep(0.5)
        if tries > 40:
            print("Can't find " + str(target))
            return False



def game_reset():
    # Storage clearing and refreshing
    mouse.position = (chrome_clear_site_data[0], chrome_clear_site_data[1])
    mouse.click(Button.left)
    time.sleep(2)
    mouse.click(Button.left)
    time.sleep(2)
    mouse.click(Button.left)
    time.sleep(2)

    mouse.position = (chrome_refresh[0], chrome_refresh[1])
    mouse.click(Button.left)

    tries = 0
    while True:
        print("Waiting for tutorial to load ( " + str(tries) + " )")
        if check_screen("main_menu_tutorial_login") == "main_menu_tutorial_login":
            break
        time.sleep(0.5)
        tries = tries + 1
        if tries > 55:
            print("Something went wrong , resetting back")
            return False

    time.sleep(1)  # loading offset

    mouse.position = (tutorial_login_button[0], tutorial_login_button[1])
    mouse.click(Button.left)
    return True
