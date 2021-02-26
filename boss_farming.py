import time

from pynput import *
from pynput.mouse import Controller, Button

from init import *

# ustawienia
mouse = Controller()
choosen_char = "1"
eq_bars = 2

# rozpoczynanie
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
time.sleep(10)

# zamykanie okna z AFK jezeli istnieje!
if check_screen("char_choose") == "afk_gain_window":
    print("AFK gains window found, closing...")
    mouse.position = (afk_claim[0], afk_claim[1])
    mouse.click(Button.left)
    time.sleep(2)

# sprawdzanie czy znajdujemy sie na dobrej mapie
mouse.position = (map[0], map[1])
mouse.click(Button.left)
time.sleep(1)
if check_screen("evf") != "EFV":
    exit("You're standing in wrong map!")
mouse.click(Button.left)
time.sleep(1)

# wchodzenie po linie
mouse.position = (EFV_rope[0], EFV_rope[1])
mouse.click(Button.left)
time.sleep(10)

# przechodzenie do obolka
mouse.position = (EFV_przejscie_do_obolka[0], EFV_przejscie_do_obolka[1])
mouse.click(Button.left)
time.sleep(10)

# przechodzenie do amarkos villa
mouse.position = (EFV_przejscie_do_amaroks_villa[0], EFV_przejscie_do_amaroks_villa[1])
mouse.click(Button.left)
time.sleep(10)

# sprawdzanie czy udało sie dojsc do wejscia
if check_screen("evf") == "amarok_entrance":
    print("Found amarok entrance dialog window!")
else:
    exit("Can't find amarok entrance dialog!")

# wchodzenie do bossa
mouse.position = (amarok_enter[0], amarok_enter[1])
mouse.click(Button.left)
time.sleep(10)

if check_screen("amarok") == "amarok_boss_head":
    print("You're in boss room! ")
else:
    exit("Whoooppp... Idk why are you not in a boss room!")

# zabij amaroka debila!
mouse.position = (amarok_click_kill[0], amarok_click_kill[1])
mouse.click(Button.left)
time.sleep(30)

# sprawdz czy amarok is ded
if check_screen("amarok") == "amarok_dead":
    print("Amarok is ded! Siara , Amarok jest ded!")
else:
    exit("Why is he still alive...")

# zmień pozycje zeby moc wszystko zlootować!
mouse.position = (amarok_loot_change_position[0], amarok_loot_change_position[1])
mouse.click(Button.left)
time.sleep(0.1)
mouse.click(Button.left)
time.sleep(10)

# przesuwanie przez loot
mouse.position = (amarok_loot_left[0], amarok_loot_left[1])
iteration = round(abs(amarok_loot_left[0] - amarok_loot_right[0]) / 10)

mouse.press(Button.left)
for i in range(iteration):
    mouse.position = (amarok_loot_left[0] + (i * 10), amarok_loot_left[1])
    time.sleep(0.05)
mouse.release(Button.left)

# sprawdz czy jest klucz w eq
mouse.position = (items[0], items[1])
mouse.click(Button.left)
time.sleep(1)

key = False
while not key:
    time.sleep(1)
    mouse.position = (eq_slotbar1[0], eq_slotbar1[1])
    mouse.click(Button.left)
    if check_screen("eq")[0] == "amarok_key":
        print("Znaleziono klucz w bag 1")
        key = True
        cords = check_screen("eq")[1]
        break
    time.sleep(1)
    mouse.position = (eq_slotbar2[0], eq_slotbar2[1])
    mouse.click(Button.left)
    if check_screen("eq")[0] == "amarok_key":
        print("Znaleziono klucz w bag 2")
        key = True
        cords = check_screen("eq")[1]
        break
    time.sleep(1)
    mouse.position = (eq_slotbar3[0], eq_slotbar3[1])
    mouse.click(Button.left)
    if check_screen("eq")[0] == "amarok_key":
        print("Znaleziono klucz w bag 3")
        key = True
        cords = check_screen("eq")[1]
        break
    time.sleep(1)
    mouse.position = (eq_slotbar4[0], eq_slotbar4[1])
    mouse.click(Button.left)
    if check_screen("eq")[0] == "amarok_key":
        print("Znaleziono klucz w bag 4")
        key = True
        cords = check_screen("eq")[1]
        break
    time.sleep(1)
    mouse.position = (eq_slotbar5[0], eq_slotbar5[1])
    mouse.click(Button.left)
    if (check_screen("eq"))[0] == "amarok_key":
        print("Znaleziono klucz w bag 5")
        key = True
        cords = check_screen("eq")[1]
        break
    print("nic nie znaleziono")
    break


if key:
    mouse.position = (cords[0]+ starting_cords[0], cords[1] +starting_cords[1])
    mouse.press(Button.left)
    time.sleep(1)
    mouse.release(Button.left)