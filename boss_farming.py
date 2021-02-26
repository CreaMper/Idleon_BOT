from moves import *

# settings
mouse = Controller()
char_slot = 1
bag_bars = 2


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

        mouse_click(EFV_rope, 0, 7)  # climbing by rope
        mouse_click(EFV_przejscie_do_obolka, 0, 10)  # run to obol

        mouse_click(EFV_przejscie_do_amaroks_villa, 0, 1)  # run to Amarok's villa

        # Check if entered successfully
        misc_wait_for_frame("loc_w1_av")
        mouse_click(amarok_enter, 0, 1)  # entering into Amarok's villa

        # Check if entered successfully
        misc_wait_for_frame("loc_w1_av_amarok_head")

        time.sleep(2)  # loading offset
        mouse_click(amarok_click_kill, 0, 1)  # just kill him bro...

        misc_wait_for_frame("loc_w1_av_amarok_dead")  # wait for Amarok to be dead

        # Change position , preparing for looting section
        mouse_click_double(amarok_loot_change_position, 0, 6)

        # Loot
        mouse_loot_swing(amarok_loot_left, amarok_loot_right)

        # Check if key dropped
        time.sleep(1)
        key = interface_eq_find_item("loc_w1_av_amarok_key", bag_bars)

        # Use that key
        if key != 0:
            # Note that there was a key
            successful = successful + 1
            # Use key
            interface_eq_use_item(key)
            # Save
            game_get_to_main_menu()
        else:
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
            print("Drop Ratio :" + str(round(float(successful / (i+1))) * 100) + "%")
        print("Run time : " + str(round((end - loop_start))) + "s")
        print("Avg run time : " + (str(round(float(time_overall / (i + 1))))) + "s")
        print("Bot uptime : " + str(round(float(time_overall / 60))) + "m")


start(2)
