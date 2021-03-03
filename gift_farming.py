from moves import *

# settings
mouse = Controller()
char_slot = 5


# ------------------------------------------------------

def start(iterations):
    successful = 0
    time_overall = 0
    for i in range(iterations):
        loop_start = time.time()

        # wait for character selection frame
        misc_wait_for_frame("main_menu_play_button")
        time.sleep(2)  # loading offset

        # click on proper character slot
        main_choose_char_slot(char_slot)

        # wait for confirmation that character was choose
        misc_wait_for_frame("main_menu_main_stats")
        main_click_play()

        # wait for menu to load
        misc_wait_for_frame("iface_menu_bar_half")
        time.sleep(2)  # loading offset

        # check if theres an AFK gains screen
        if check_if_frame_exists_optional("iface_afk_gain_button", "AFK Gains"):
            mouse_click(afk_claim, 0, 2)

        # attack click and use box spell
        mouse_click(attacks, 0, 1)
        mouse_click(attack_slot_1, 0, 1)

        # move mouse
        mouse_click(starting_cords,0,2)

        # check if its successful or not
        if check_if_frame_exists_optional("skill_present_on", "Present CD disappeared!"):
            successful = successful + 1

            # Loot
            mouse_loot_swing(SM_spawn_loot_left, SM_spawn_loot_right)

            # Open main bar
            mouse_click(attacks, 0, 1)
            # Save
            game_get_to_main_menu()

        # Restart
        while True:
            if game_reset():
                break

        end = time.time()
        time_overall = time_overall + (end - loop_start)
        # Stats ------------------------------------------------------
        print("Try " + str(i + 1) + "/" + str(iterations))
        print("Successfully : " + str(successful))
        if successful == 0:
            print("Drop Ratio : 0%")
        else:
            print("Drop Ratio :" + str(round(float(successful / (i + 1))) * 100) + "%")
        print("Run time : " + str(round((end - loop_start))) + "s")
        print("Avg run time : " + (str(round(float(time_overall / (i + 1))))) + "s")
        print("Bot uptime : " + str(round(float(time_overall / 60))) + "m")

start(2)
