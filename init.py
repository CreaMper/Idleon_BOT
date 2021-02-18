from ctypes import windll, Structure, c_long, byref
import keyboard as keyboard
import win32api
import win32gui
import win32ui
import numpy as np
from PIL import ImageGrab
import cv2
from mousee import *
from resolution import *
import PIL

global starting_cords, click, found_coords

global char1, char2, char3, char4, char5, login_start
global afk_claim, chrome_clear_site_data, chrome_refresh, tutorial_login_button
global map, items, attacks, menu, menu_swap_players, menu_swap_players_player_menu, attack_slot_1
global eq_slotbar1, eq_slotbar2, eq_slotbar3, eq_slotbar4, eq_slotbar5
global EFV_rope, EFV_przejscie_do_obolka, EFV_przejscie_do_amaroks_villa
global amarok_enter, amarok_click_kill, amarok_loot_change_position, amarok_loot_left, amarok_loot_right
global JB_spawn, JB_sprawn_loot_left, JB_sprawn_loot_right

def check(target):
    dc = win32gui.GetDC(0)
    dcObj = win32ui.CreateDCFromHandle(dc)
    hwnd = win32gui.WindowFromPoint((0, 0))
    monitor = (0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))

    while True:
        dcObj.Rectangle((target[0], target[1], target[0] + 30, target[1] + 30))
        win32gui.InvalidateRect(hwnd, monitor, True)  # Refresh the entire monitor


def calculate_obj_in_view_position(x, y):
    # 176,315

    # wybor postaci
    global char1, char2, char3, char4, char5, login_start
    char1 = (x + 64, y + 407)  # 1st char
    char2 = (x + 194, y + 407)  # 2nd char
    char3 = (x + 328, y + 407)  # 3rd char
    char4 = (x + 588, y + 407)  # 4th char
    char5 = (x + 714, y + 407)  # 5th char
    login_start = (x + 924, y + 404)  # start

    # misc
    global afk_claim, chrome_clear_site_data, chrome_refresh, tutorial_login_button
    afk_claim = (x + 594, y + 294)  # click when afk gains shows up
    chrome_clear_site_data = (1610, 497)
    chrome_refresh = (86, 52)
    tutorial_login_button = (x + 951, y + 30)

    # interface
    global map, items, attacks, menu, menu_swap_players, menu_swap_players_player_menu, attack_slot_1
    map = (x + 803, y + 528)  # mapa na pasku
    items = (x + 601, y + 523)
    attacks = (x + 521, y + 525)
    attack_slot_1 = (x + 597, y + 528)
    menu = (x + 949, y + 524)
    menu_swap_players = (x + 924, y + 340)
    menu_swap_players_player_menu = (x + 285, y + 77)

    # eq #64
    global eq_slotbar1, eq_slotbar2, eq_slotbar3, eq_slotbar4, eq_slotbar5
    eq_slotbar1 = (x + 682, y + 107)
    eq_slotbar2 = (x + 746, y + 107)
    eq_slotbar3 = (x + 810, y + 107)
    eq_slotbar4 = (x + 874, y + 107)
    eq_slotbar5 = (x + 938, y + 107)

    # amarok
    global amarok_enter, amarok_click_kill, amarok_loot_change_position, amarok_loot_left, amarok_loot_right
    amarok_enter = (x + 769, y + 175)
    amarok_click_kill = (x + 878, y + 385)
    amarok_loot_change_position = (x + 783, y + 424)
    amarok_loot_left = (x + 144, y + 410)
    amarok_loot_right = (x + 847, y + 414)

    # Encroaching_forest_villas EFV
    global EFV_rope, EFV_przejscie_do_obolka, EFV_przejscie_do_amaroks_villa
    EFV_rope = (x + 70, y + 245)  # resp -> linka
    EFV_przejscie_do_obolka = (x + 945, y + 249)  # nad linka -> obolki
    EFV_przejscie_do_amaroks_villa = (x + 973, y + 308)  # obolki -> amaroks_villa

    # Jar bridge JB
    global JB_spawn, JB_sprawn_loot_left, JB_sprawn_loot_right
    JB_spawn = (x + 672, y + 351)
    # 813,665 | 901, 670
    JB_sprawn_loot_left = (x  +637, y + 350)
    JB_sprawn_loot_right = (x  +725, y + 355)



def check_screen(frame):
    # inicjalizacja
    screenshoot = np.array(
        ImageGrab.grab(
            bbox=(starting_cords[0], starting_cords[1], starting_cords[0] + 989, starting_cords[1] + 555))
            .convert("RGB"))
    screenshoot_cv2 = cv2.cvtColor(np.array(screenshoot), cv2.COLOR_BGR2RGB)

    # dodawanie_rsc
    play_button = cv2.imread("rsc/play.png")
    afk_gain_button = cv2.imread("rsc/afk_gain_button.png")
    map_name_EFV = cv2.imread("rsc/map_names/encroaching_forest_villas.png")
    amarok_entrance = cv2.imread("rsc/amarok/amaroks_villa.png")
    amarok_boss_head = cv2.imread("rsc/amarok/amarok_head.png")
    amarok_boss_dead = cv2.imread("rsc/amarok/amarok_dead.png")
    amarok_key = cv2.imread("rsc/amarok/amarok_key.png")
    map_name_JB = cv2.imread("rsc/map_names/jar_bridge.png")
    skills_present_on = cv2.imread("rsc/skills/present_on.png")
    skills_present_off = cv2.imread("rsc/skills/present_off.png")
    menu_bar_half = cv2.imread("rsc/menu_bar_half.png")
    tutorial_log_in = cv2.imread("rsc/tutorial_log_in.png")

    # misc
    global click
    threshold = .95
    click = (0, 0)

    # funkcja sprawdzająca
    def check_if_exist(rescource):
        global click
        click = None
        res = cv2.matchTemplate(screenshoot_cv2, rescource, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screenshoot_cv2, pt, (pt[0] + 30, pt[1] + 30), (0, 0, 255), 2)
            click = pt[0], pt[1]
        if click is None:
            return 0
        else:
            return 1



    # sprawdzenie widoków
    if frame == "char_choose":
        if check_if_exist(play_button) == 1:  # wybór postaci
            return "char_select"
        elif check_if_exist(afk_gain_button) == 1:
            return "afk_gain_window"
        else:
            return 0

    if frame == "evf":
        if check_if_exist(map_name_EFV) == 1:
            return "EFV"
        elif check_if_exist(amarok_entrance) == 1:
            return "amarok_entrance"
        else:
            return 0

    if frame == "jb":
        if check_if_exist(map_name_JB) == 1:
            return "JB"
        else:
            return 0

    if frame == "skill_bar":
        if check_if_exist(skills_present_on) == 1:
            return "present_on"
        elif check_if_exist(skills_present_off) == 1:
            return "present_off"
        else:
            return 0

    if frame == "amarok":
        if check_if_exist(amarok_boss_head) == 1:
            return "amarok_boss_head"
        elif check_if_exist(amarok_boss_dead) == 1:
            return "amarok_dead"
        else:
            return 0

    if frame == "eq":
        if check_if_exist(amarok_key) == 1:
            return "amarok_key", click
        else:
            return 0

    if frame == "interface":
        if check_if_exist(menu_bar_half):
            return "menu_bar_half"
        if check_if_exist(tutorial_log_in):
            return "tutorial_login"
        else:
            return 0

# zbieranie infromacji
while True:
    try:
        # if keyboard.is_pressed('p'):  # if key 'q' is pressed
        print('Got starting position')
        # cords = Mouse().queryMousePosition()
        starting_cords = [176, 315]
        calculate_obj_in_view_position(starting_cords[0], starting_cords[1])

        break
    except:
        print("Błąd podczas zbierania informacji o pozycji, ponawianie...")
