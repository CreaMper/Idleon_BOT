global char1, char2, char3, char4, char5, login_start
global afk_claim, chrome_clear_site_data, chrome_refresh, tutorial_login_button
global map, items, attacks, menu, menu_swap_players, menu_swap_players_player_menu, attack_slot_1
global eq_slotbar1, eq_slotbar2, eq_slotbar3, eq_slotbar4, eq_slotbar5
global EFV_rope, EFV_przejscie_do_obolka, EFV_przejscie_do_amaroks_villa
global amarok_enter, amarok_click_kill, amarok_loot_change_position, amarok_loot_left, amarok_loot_right
global JB_spawn, JB_sprawn_loot_left, JB_sprawn_loot_right
global SM_spawn_loot_left, SM_spawn_loot_right


def calculate_obj_in_view_position(x, y):
    # starting pos 176,315

    # slot choosing
    global char1, char2, char3, char4, char5, login_start
    char1 = (x + 64, y + 407)  # 1st char
    char2 = (x + 194, y + 407)  # 2nd char
    char3 = (x + 328, y + 407)  # 3rd char
    char4 = (x + 459, y + 407)  # 4th char
    char5 = (x + 589, y + 407)  # 5th char
    char6 = (x + 714, y + 407)  # 6th char
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

    # amaroks_villa
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
    JB_sprawn_loot_left = (x + 637, y + 350)
    JB_sprawn_loot_right = (x + 725, y + 355)

    # Spore Meadows SM
    global SM_spawn_loot_left, SM_spawn_loot_right
    SM_spawn_loot_left = (x + 659, y + 114)
    SM_spawn_loot_right = (x + 783, y + 114)
