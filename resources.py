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
    threshold = .90

    # Function that check if theres an targeted obj in frame
    global click
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

    # MINIGAMES
    rsc_minigame_play_button = cv2.imread("resources/images/interface/minigames/minigame_play_game.png")
    rsc_minigame_wood_leaf = cv2.imread("resources/images/interface/minigames/wood/minigame_wood_leaf.png")

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


    # Checking for objects
    # INTERFACE
    if frame == "iface_afk_gain_button":
        if check_if_exist(rsc_iface_afk_gain_button):
            return frame, click
    if frame == "iface_menu_bar_half":
        if check_if_exist(rsc_iface_menu_bar_half):
            return frame, click
    if frame == "iface_menu_swap_players":
        if check_if_exist(rsc_iface_menu_swap_players):
            return frame, click
    if frame == "iface_menu_swap_players_player_menu":
        if check_if_exist(rsc_iface_menu_swap_players_player_menu):
            return frame, click

    # SKILLS
    if frame == "skill_present_on":
        if check_if_exist(rsc_skill_present_on):
            return frame, click
    if frame == "skill_present_off":
        if check_if_exist(rsc_skill_present_off):
            return frame, click

    # MAIN MENU
    if frame == "main_menu_play_button":
        if check_if_exist(rsc_main_menu_play_button):
            return frame, click
    if frame == "main_menu_main_stats":
        if check_if_exist(rsc_main_menu_main_stats):
            return frame, click
    if frame == "main_menu_tutorial_login":
        if check_if_exist(rsc_main_menu_tutorial_login):
            return frame, click

    # MINIGAMES
    if frame == "minigame_play_button":
        if check_if_exist(rsc_minigame_play_button):
            return frame, click

    if frame == "minigame_wood_leaf":
        if check_if_exist(rsc_minigame_wood_leaf):
            return frame, click

    # LOCATIONS
    # WORLD 1

    # AMAROK'S VILLA
    if frame == "loc_w1_av":
        if check_if_exist(rsc_loc_w1_av):
            return frame, click
    if frame == "loc_w1_av_amarok_head":
        if check_if_exist(rsc_loc_w1_av_amarok_head):
            return frame, click
    if frame == "loc_w1_av_amarok_dead":
        if check_if_exist(rsc_loc_w1_av_amarok_dead):
            return frame, click
    if frame == "loc_w1_av_amarok_key":
        if check_if_exist(rsc_loc_w1_av_amarok_key):
            return frame, click
        else:
            return "0", "0"

    # ENCROACHING FORES VILLAS
    if frame == "loc_w1_efv_map_name":
        if check_if_exist(rsc_loc_w1_efv_map_name):
            return frame, click
    if frame == "loc_w1_efv_upper_rope":
        if check_if_exist(rsc_loc_w1_efv_upper_rope):
            return frame, click

    # WORLD 2
    # JAR BRIDGE
    if frame == "loc_w2_jb_map_name":
        if check_if_exist(rsc_loc_w2_jb_map_name):
            return frame, click

    return False
