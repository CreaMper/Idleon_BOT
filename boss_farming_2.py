import time
from pynput import *
from pynput.mouse import Controller, Button
from init import *
from moves import *

# ustawienia

mouse = Controller()
choosen_char = 1
bag_bars = 2


# ------------------------------------------------------

def start(iterations):
    succeful = 0
    laczny_czas = 0
    for i in range(iterations):
        start = time.time()

        # czekaj az najdzie dobry frame
        misc_wait_for_frame("char_choose", "char_select")
        time.sleep(2) # offset ładowania
        # oczekuj na klikniecie i proceduj dalej
        main_choose_char_slot(choosen_char)

        # czekaj az pojawi się potwierdzenie wybrania postaci i kliknij dalej
        misc_wait_for_frame("main_stats", "main_stats")
        main_click_play()

        # czekaj na zaladowanie menu
        misc_wait_for_frame("interface", "menu_bar_half")
        time.sleep(2)  # offset bo afk gains pojawia sie chwile pozniej

        # check if theres an AFK gains screen
        if check_if_frame_exists_optional("char_choose", "afk_gain_window", "AFK Gains"):
            mouse_click(afk_claim, 0, 2)

        mouse_click(EFV_rope, 0, 7)  # wchodzenie po linie
        mouse_click(EFV_przejscie_do_obolka, 0, 10)  # przechodzenie do obolka

        mouse_click(EFV_przejscie_do_amaroks_villa, 0, 1)  # przechodzenie do amarkos villa

        # sprawdzanie czy udało sie dojsc do wejscia
        misc_wait_for_frame("evf", "amarok_entrance")
        mouse_click(amarok_enter, 0, 1)  # wchodzenie do bossa

        # sprawdzanie czy jestes w boosroom
        misc_wait_for_frame("amarok", "amarok_boss_head")

        time.sleep(2)  # offset na ładowanie
        mouse_click(amarok_click_kill, 0, 1)  # zabij amaroka debila!

        misc_wait_for_frame("amarok_2", "amarok_dead")  # czekaj az amarok bedzie dead

        # zmień pozycje zeby moc wszystko zlootować!
        mouse_click_double(amarok_loot_change_position, 0, 6)

        # przesuwanie przez loot
        mouse_loot_swing(amarok_loot_left, amarok_loot_right)

        # sprawdz czy jest klucz w eq , zapisz jego kordy
        time.sleep(1)
        key = interface_eq_find_item("amarok_key", bag_bars)

        # uzyj przedmiotu
        if key != 0:
            # zaznaczenie , iż próba jest udana
            succeful = succeful + 1
            # użycie klucza
            interface_eq_use_item(key)
            # zapisywanie postępów
            game_get_to_main_menu()
        else:
            # resetowanie do stanu początkowego
            while True:
                if game_reset():
                    break

        end = time.time()
        laczny_czas = laczny_czas + (end - start)
        # statystyki ------------------------------------------------------
        print("Try " + str(i+1) + "/" + str(iterations))
        print("Successfully : " + str(succeful))
        if succeful == 0:
            print("Drop Ratio : 0%")
        else:
            print("Drop Ratio :" + str(round(float(succeful / i))) + "%")
        print("Run time : " + str(round((end - start))) + "s")
        print("Avg run time : " + (str(round(float(laczny_czas / (i + 1))))) + "s")
        print("Bot uptime : " + str(round(float(laczny_czas/60))) + "m")


start(3)
