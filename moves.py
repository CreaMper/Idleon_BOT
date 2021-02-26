import time

from pynput.mouse import Controller, Button

from init import check_screen, char1, char2, char3, char4, char5, login_start, afk_claim, items, eq_slotbar1, \
    eq_slotbar2, eq_slotbar3, eq_slotbar4, eq_slotbar5, starting_cords, menu, menu_swap_players, \
    menu_swap_players_player_menu, chrome_clear_site_data, tutorial_login_button, chrome_refresh

mouse = Controller()


def check_if_frame_exists(cat, target, desc):
    """
    :param cat:  which frame category we are looking for
    :param target: what element in that category we are looking for
    :param desc: description that will be printed after function ends
    """
    if check_screen(cat) == target:
        print(desc + " Found!")
        return True
    else:
        exit(desc + " Not Found!")


def check_if_frame_exists_optional(cat, target, desc):
    """
    :param cat:  which frame category we are looking for
    :param target: what element in that category we are looking for
    :param desc: description that will be printed after function ends
    :param return: returns true if  frame was found
    """
    if check_screen(cat) == target:
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
    print("Play button clicked")


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
    if check_screen("eq")[0] == item:
        print("amarok_key" + "Found at slotbar 1")
        cords = check_screen("eq")[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]
    if bags == 1:
        return False

    mouse.position = (eq_slotbar2[0], eq_slotbar2[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen("eq")[0] == item:
        print(item + "Found at slotbar 2")
        cords = check_screen("eq")[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]
    if bags == 2:
        return False

    mouse.position = (eq_slotbar3[0], eq_slotbar3[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen("eq")[0] == item:
        print(item + "Found at slotbar 3")
        cords = check_screen("eq")[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]
    if bags == 3:
        return False

    mouse.position = (eq_slotbar4[0], eq_slotbar4[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen("eq")[0] == item:
        print(item + "Found at slotbar 4")
        cords = check_screen("eq")[1]
        return cords[0] + starting_cords[0], cords[1] + starting_cords[1]
    if bags == 4:
        return False

    mouse.position = (eq_slotbar5[0], eq_slotbar5[1])
    mouse.click(Button.left)
    time.sleep(1)
    if check_screen("eq")[0] == item:
        print(item + "Found at slotbar 5")
        cords = check_screen("eq")[1]
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
        if check_screen("reload") == "menu_swap_players":
            break
        time.sleep(0.5)

    mouse.position = (menu_swap_players[0], menu_swap_players[1])
    time.sleep(0.5)
    mouse.click(Button.left)

    while True:
        if check_screen("reload") == "menu_swap_players_player_menu":
            break
        time.sleep(0.5)

    mouse.position = (menu_swap_players_player_menu[0], menu_swap_players_player_menu[1])
    time.sleep(0.5)
    mouse.click(Button.left)

    while True:
        if check_screen("char_choose") == "char_select":
            break
        time.sleep(0.5)


def misc_wait_for_frame(cat, target):
    """
    :param cat: category of frames
    :param target: what to looking for
    :return:
    """
    while True:
        print(check_screen(cat), cat, target)
        if check_screen(cat) == target:
            break
        time.sleep(0.5)


def game_reset():
    # czyszczenie pamięci i odswiezanie strony
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
        print(check_screen("interface"), "interface", "tutorial_login ", tries)
        if check_screen("interface") == "tutorial_login":
            break
        time.sleep(0.5)
        tries = tries + 1
        if tries > 55:
            print("Something went wrong , reseting back")
            return False

    time.sleep(1)  # offset ładowania

    mouse.position = (tutorial_login_button[0], tutorial_login_button[1])
    mouse.click(Button.left)
    return True
