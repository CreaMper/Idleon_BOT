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

# sprawdz czy dobrze znalazło ekran
check_if_frame_exists("char_choose", "char_select", "Char screen")

# oczekuj na klikniecie i proceduj dalej
main_choose_char_slot(choosen_char)

# czekaj az pojawi się potwierdzenie wybrania postaci i kliknij dalej
misc_wait_for_frame("main_stats", "main_stats")
main_click_play()

# czekaj na zaladowanie menu
misc_wait_for_frame("interface", "menu_bar_half")

# check if theres an AFK gains screen
if check_if_frame_exists_optional("char_choose", "afk_gain_window", "AFK Gains"):
    mouse_click(afk_claim, 0, 2)

mouse_click(EFV_rope, 0, 10)  # wchodzenie po linie
mouse_click(EFV_przejscie_do_obolka, 0, 10)  # przechodzenie do obolka

mouse_click(EFV_przejscie_do_amaroks_villa, 0, 10)  # przechodzenie do amarkos villa

# sprawdzanie czy udało sie dojsc do wejscia
check_if_frame_exists("evf", "amarok_entrance", "Amarok's entrance")

mouse_click(amarok_enter, 0, 10)  # wchodzenie do bossa

# sprawdzanie czy jestes w boosroom
check_if_frame_exists("amarok", "amarok_boss_head", "Amarok's entrance")

mouse_click(amarok_click_kill, 0, 30)  # zabij amaroka debila!

check_if_frame_exists("amarok", "amarok_dead", "Amarok's dead body")  # sprawdz czy amarok is ded

# zmień pozycje zeby moc wszystko zlootować!
mouse_click_double(amarok_loot_change_position, 0, 10)

# przesuwanie przez loot
mouse_loot_swing(amarok_loot_left, amarok_loot_right)

# sprawdz czy jest klucz w eq , zapisz jego kordy
time.sleep(1)
key = interface_eq_find_item("amarok_key")
print(key)
# uzyj przedmiotu
if key != 0:
    # użycie klucza
    interface_eq_use_item(key)
    # zapisywanie postępów
    game_get_to_main_menu()
