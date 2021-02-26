import time
import timeit

from pynput import *
from pynput.mouse import Controller, Button

from init import *

# ustawienia
mouse = Controller()
choosen_char = "4"

def box_farming(iterations):
    succeful = 0
    laczny_czas = 0
    for i in range(iterations):
        start = time.time()
        time.sleep(2)
        # wybor postaci
        if check_screen("char_choose") == "char_select":
            print("Found character choosing screen")
        else:
            exit("Choosign screen not found")

        # wybor postaci
        if choosen_char == "1":
            mouse.position = (char1[0], char1[1])
        elif choosen_char == "2":
            mouse.position = (char2[0], char2[1])
        elif choosen_char == "3":
            mouse.position = (char3[0], char3[1])
        elif choosen_char == "4":
            mouse.position = (char4[0], char4[1])
        elif choosen_char == "5":
            mouse.position = (char5[0], char5[1])

        mouse.click(Button.left)
        time.sleep(0.5)
        mouse.position = (login_start[0], login_start[1])
        time.sleep(0.5)
        mouse.click(Button.left)
        time.sleep(0.5)

        print("Choosed slot ", choosen_char)

        #oczekiwanie na zaladowanie game frame
        temp = 1
        hardmode_2 = False
        while (True):
            time.sleep(2)
            if check_screen("interface") == "menu_bar_half":
                print("Game screen loaded")
                break
            print("Waiting for game screen to load! (" + str(temp) + ")")
            temp = temp + 1
            if temp > 20:
                print("Can't find game screen! Trying to fix it!")
                hardmode_2 = True
                break

        while True:
            if not hardmode_2:
                break
            if hardmode_2:
                # czyszczenie pamięci i odswiezanie strony
                mouse.position = (chrome_clear_site_data[0], chrome_clear_site_data[1])
                mouse.click(Button.left)
                time.sleep(1)
                mouse.click(Button.left)
                time.sleep(1)
                mouse.click(Button.left)
                time.sleep(1)

                mouse.position = (chrome_refresh[0], chrome_refresh[1])
                mouse.click(Button.left)

                # wybor postaci
                if choosen_char == "1":
                    mouse.position = (char1[0], char1[1])
                elif choosen_char == "2":
                    mouse.position = (char2[0], char2[1])
                elif choosen_char == "3":
                    mouse.position = (char3[0], char3[1])
                elif choosen_char == "4":
                    mouse.position = (char4[0], char4[1])
                elif choosen_char == "5":
                    mouse.position = (char5[0], char5[1])

                mouse.click(Button.left)
                time.sleep(0.5)
                mouse.position = (login_start[0], login_start[1])
                time.sleep(0.5)
                mouse.click(Button.left)
                time.sleep(0.5)

                while (True):
                    time.sleep(1)
                    if check_screen("interface") == "menu_bar_half":
                        print("Game screen loaded")
                        break
                    print("Waiting for game screen to load! (" + str(temp) + ")")
                    temp = temp + 1
                    if temp == 20:
                        print("Can't find game screen! Trying to fix it!")
                        hardmode_2 = True
                        break
                    break

        # zamykanie okna z AFK jezeli istnieje!
        if check_screen("char_choose") == "afk_gain_window":
            print("AFK gains window found, closing...")
            mouse.position = (afk_claim[0], afk_claim[1])
            mouse.click(Button.left)
            time.sleep(2)


        #odpalanie prezentu
        mouse.position = (attacks[0], attacks[1])
        mouse.click(Button.left)
        time.sleep(1)

        mouse.position = (attack_slot_1[0], attack_slot_1[1])
        mouse.click(Button.left)
        time.sleep(1)

        mouse.position = (starting_cords[0]+30, starting_cords[1]+30) #zabieranie myszki
        mouse.click(Button.left)

        time.sleep(3) #czekanie na prezent

        ok = False

        if check_screen("skill_bar") == "present_on":
            print("Present is available!")
            ok = True

        if check_screen("skill_bar") == "present_off":
            print("Present is on cooldown , e.g. is not available!")
            ok = False

        if ok:
            mouse.position = (JB_sprawn_loot_left[0], JB_sprawn_loot_right[1])
            iteration = round(abs(JB_sprawn_loot_left[0] - JB_sprawn_loot_right[0]) / 10)

            mouse.press(Button.left)
            for i in range(iteration):
                mouse.position = (JB_sprawn_loot_left[0] + (i * 10), JB_sprawn_loot_right[1])
                time.sleep(0.05)
            mouse.release(Button.left)

            mouse.position = (attacks[0], attacks[1]) #odklikanie ataku
            mouse.click(Button.left)
            time.sleep(1)

            mouse.position = (menu[0], menu[1])
            mouse.click(Button.left)
            time.sleep(1)

            mouse.position = (menu_swap_players[0], menu_swap_players[1])
            mouse.click(Button.left)
            time.sleep(1)

            mouse.position = (menu_swap_players_player_menu[0], menu_swap_players_player_menu[1])
            mouse.click(Button.left)

            #oczekiwanie na załadowanie się ekranu postaci // zapisanie postepu
            temp = 1
            while (True):
                time.sleep(1)
                if check_screen("char_choose") == "char_select":
                    print("Character screen loaded!")
                    break
                print("Waiting for character screen to load! (" + str(temp) + ")")
                temp = temp + 1
                if temp == 20:
                    exit("Can't find character screen!")
            time.sleep(2) #oczekiwanie na zapisanie przez firebase


        #czyszczenie pamięci i odswiezanie strony
        mouse.position = (chrome_clear_site_data[0], chrome_clear_site_data[1])
        mouse.click(Button.left)
        time.sleep(2)
        mouse.click(Button.left)
        time.sleep(2)
        mouse.click(Button.left)
        time.sleep(2)

        mouse.position = (chrome_refresh[0], chrome_refresh[1])
        mouse.click(Button.left)

        # oczekiwanie na załadowanie się tutorialu // zapisanie postepu
        hard_mode = False
        temp = 1
        while (True):
            time.sleep(1)
            if check_screen("interface") == "tutorial_login":
                print("Tutorial view reached!!")
                break
            print("Still waiting for tutorial to load! (" + str(temp) + ")")
            temp = temp + 1
            if temp == 30:
                print("Can't find tutorial screen! Trying to fixing it!")
                hard_mode = True
                break

        while True:
            if not hard_mode:
                break
            if hard_mode:
                # czyszczenie pamięci i odswiezanie strony
                mouse.position = (chrome_clear_site_data[0], chrome_clear_site_data[1])
                mouse.click(Button.left)
                time.sleep(1)
                mouse.click(Button.left)
                time.sleep(1)
                mouse.click(Button.left)
                time.sleep(1)

                mouse.position = (chrome_refresh[0], chrome_refresh[1])
                mouse.click(Button.left)

                # oczekiwanie na załadowanie się tutorialu // zapisanie postepu
                temp = 1
                while (True):
                    time.sleep(1)
                    if check_screen("interface") == "tutorial_login":
                        print("Tutorial view reached!!")
                        break
                    print("Still waiting for tutorial to load! (" + str(temp) + ")")
                    temp = temp + 1
                    if temp == 30:
                        print("Can't find tutorial screen! Trying to fixing it!")
                        hard_mode = True
                        break
                break

        #logowanie powtórne
        mouse.position = (tutorial_login_button[0], tutorial_login_button[1])
        mouse.click(Button.left)

        # oczekiwanie na załadowanie się ekranu postaci // zapisanie postepu
        temp = 1
        while (True):
            time.sleep(1)
            if check_screen("char_choose") == "char_select":
                print("Character screen loaded!")
                break
            print("Waiting for character screen to load! (" + str(temp) + ")")
            temp = temp + 1
            if temp == 20:
                exit("Can't find character screen!")
        time.sleep(1)

        end = time.time()
        if ok:
            print("Petla ("+str(i+1)+"/" +str(iterations) +") zakończona sukcesem i wykonana w czasie " + str(round((end - start))) + "s")
            succeful = succeful +1
            laczny_czas = laczny_czas + (end - start)
        else:
            print("Petla ("+str(i+1)+"/" +str(iterations) +") zakończona porazka i wykonana w czasie " + str(round((end - start))) + "s")
            laczny_czas = laczny_czas + (end - start)

        print("RAPORT---------")
        print("Operacje : " + str(i+1))
        print("Udane : " + str(succeful))
        if i == 0:
            print("DropRatio : 0 %")
        else:
            print("DropRatio : " + str(round(float(succeful / i) * 100)) + " %")
        print("Time : " + str(round(float(laczny_czas / 60))) + " mins")
        print("Sredni czas na operacje : " + (str(float(round(laczny_czas / (i+1))))) + "s")



box_farming(50000)
