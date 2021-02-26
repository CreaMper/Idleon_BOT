import numpy as np
from PIL import ImageGrab
import cv2
from init import *
global starting_cords, click, found_coords


def check_screen(frame):
    # initialisation
    screenshot = np.array(
        ImageGrab.grab(
            bbox=(starting_cords[0], starting_cords[1], starting_cords[0] + 989, starting_cords[1] + 555))
            .convert("RGB"))
    screenshot_cv2 = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)

    # Settings and misc
    threshold = .85

    # RSC loading -----------------------------------------------------------------
    # INTERFACE
    rsc_iface_afk_gain_button = cv2.imread("resources/images/interface/in_game/afk_gain_button.png")
    rsc_iface_menu_bar_half = cv2.imread("resources/images/interface/in_game/menu_bar_half.png")
    rsc_iface_menu_swap_players = cv2.imread("resources/images/interface/in_game/menu_swap_players.png")
    rsc_iface_menu_swap_players_player_menu = cv2.imread(
        "resources/images/interface/in_game/menu_swap_players_player_menu.png")

    # SKILLS
    rsc_skill_present_on = cv2.imread("resources/images/skills/present_on.png")
    rsc_skill_present_off = cv2.imread("resources/images/skills/present_off.png")

    # MAIN MENU
    rsc_main_menu_play_button = cv2.imread("resources/images/interface/main_menu/play.png")
    rsc_main_menu_main_stats = cv2.imread("resources/images/interface/main_menu/main_stats.png")
    rsc_main_menu_tutorial_login = cv2.imread("resources/images/interface/main_menu/tutorial_log_in.png")

    # LOCATIONS
    # WORLD 1

    # AMAROK'S VILLA
    rsc_loc_w1_av = cv2.imread("resources/images/locations/W1/amaroks_villa/amaroks_villa.png")
    rsc_loc_w1_av_amarok_head = cv2.imread("resources/images/locations/W1/amaroks_villa/amarok_head.png")
    rsc_loc_w1_av_amarok_dead = cv2.imread("resources/images/locations/W1/amaroks_villa/amarok_dead.png")
    rsc_loc_w1_av_amarok_key = cv2.imread("resources/images/locations/W1/amaroks_villa/amarok_key.png")

    # ENCROACHING FORES VILLAS
    rsc_loc_w1_efv_map_name = cv2.imread("resources/images/locations/W1/EFV/encroaching_forest_villas.png")
    rsc_loc_w1_efv_upper_rope = cv2.imread("resources/images/locations/W1/EFV/upper_rope.png")

    # WORLD 2
    # JAR BRIDGE
    rsc_loc_w2_jb_map_name = cv2.imread("resources/images/map_names/jar_bridge.png")

    # Check frame for a resource
    global click
    threshold = .85
    click = (0, 0)

    def check_if_exist(resource):
        global click
        click = None
        res = cv2.matchTemplate(screenshot_cv2, resource, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screenshot_cv2, pt, (pt[0] + 30, pt[1] + 30), (0, 0, 255), 2)
            click = pt[0], pt[1]
        if click is None:
            return False
        else:
            return True

    # sprawdzenie widoków
    if frame == "char_choose":
        if check_if_exist(rsc_main_menu_play_button) == 1:  # wybór postaci
            return "char_select"
        elif check_if_exist(rsc_iface_afk_gain_button) == 1:
            return "afk_gain_window"
        elif check_if_exist(rsc_main_menu_main_stats) == 1:
            return "main_stats"
        else:
            return 0

    if frame == "main_stats":
        if check_if_exist(rsc_main_menu_main_stats) == 1:
            return "main_stats"
        else:
            return 0

    if frame == "evf":
        if check_if_exist(rsc_loc_w1_efv_map_name) == 1:
            return "EFV"
        elif check_if_exist(rsc_loc_w1_av) == 1:
            return "amarok_entrance"
        else:
            return 0

    if frame == "jb":
        if check_if_exist(rsc_loc_w2_jb_map_name) == 1:
            return "JB"
        else:
            return 0

    if frame == "skill_bar":
        if check_if_exist(rsc_skill_present_on) == 1:
            return "present_on"
        elif check_if_exist(rsc_skill_present_off) == 1:
            return "present_off"
        else:
            return 0

    if frame == "amaroks_villa":
        if check_if_exist(rsc_loc_w1_av_amarok_head) == 1:
            return "amarok_boss_head"
        else:
            return 0

    if frame == "amarok_2":
        if check_if_exist(rsc_loc_w1_av_amarok_dead) == 1:
            return "amarok_dead"
        else:
            return 0

    if frame == "eq":
        if check_if_exist(rsc_loc_w1_av_amarok_key) == 1:
            return "amarok_key", click
        else:
            return "0", "0"

    if frame == "interface":
        if check_if_exist(rsc_iface_menu_bar_half) == 1:
            return "menu_bar_half"
        if check_if_exist(rsc_main_menu_tutorial_login) == 1:
            return "tutorial_login"
        else:
            return 0

    if frame == "reload":
        if check_if_exist(rsc_iface_menu_swap_players_player_menu) == 1:
            return "menu_swap_players_player_menu"
        if check_if_exist(rsc_iface_menu_swap_players) == 1:
            return "menu_swap_players"
        else:
            return 0

    if frame == "efv_2":
        if check_if_exist(rsc_loc_w1_efv_upper_rope) == 1:
            return "efv_rope"
