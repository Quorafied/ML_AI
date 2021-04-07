import pyautogui
import pydirectinput
import time
import cv2 as cv

pyautogui.FAILSAFE = False

time.sleep(3)

print(pyautogui.position())

# count = 0
# wins = 0
# points = 0
# loses = 0
tries = 0

# -----------------------------------------

def waitForScreen(obj):
    tries = 0
    while True:
        print("Looking for {}".format(str(obj)))
        if pyautogui.locateOnScreen("{}.png".format(str(obj)), confidence=0.8):
            time.sleep(0.5)
            coords = pyautogui.locateOnScreen("{}.png".format(str(obj)), confidence=0.8)

            (x, y) = pyautogui.position()
            pyautogui.click(coords)
            pyautogui.moveTo(x, y)
            break
        else:
            time.sleep(0.3)

            tries += 1
            print(str(tries))
            if tries > 300:
                break


# ------------------------------------------


def Buy_100_Rare():
    time.sleep(3)
    print("3 seconds to place cursor on Cell_Purchase_Button")

    for clicks in range(100): # Loops 100 times.
        pydirectinput.click()    # Simulates a left mouse click at cursor position.
        print(clicks)
    """Debug"""

def PvP_AutoThrough():
    count = -1
    points = 0
    wins = 0
    loses = 0


    T1_EGG_C = 0
    T2_EGG_C = 0    
    T3_EGG_C = 0    
    T4_EGG_C = 0    
    T5_EGG_C = 0    
    T6_EGG_C = 0    
    T7_EGG_C = 0     

    LIST_EGGS = ["PVP_Samples/T1_EGG.png",
                 "PVP_Samples/T2_EGG.png",
                 "PVP_Samples/T3_EGG.png",
                 "PVP_Samples/T4_EGG.png",
                 "PVP_Samples/T5_EGG.png"
                 ]
    def Check_Egg(t1c, t2c, t3c, t4c, t5c):
        for egg in LIST_EGGS:
            if pyautogui.locateOnScreen(egg, confidence=0.95):
                if egg[13] == "1":
                    return 1
                if egg[13] == "2":
                    return 2
                if egg[13] == "3":
                    return 3
                if egg[13] == "4":
                    return 4
                if egg[13] == "5":
                    return 5
                #if egg[13] == "6":
                #    t6c += 1
                #if egg[13] == "7":
                #    t7c += 1

    def Output_Eggs(t1c, t2c, t3c, t4c, t5c):
        print("Tier1: {}, Tier2: {}, Tier3: {}, Tier4: {}, Tier5: {}, Tier6: , Tier7: ".format(t1c, t2c, t3c, t4c, t5c))

    

    #"PVP_Samples/T6_EGG.png"
    #"PVP_Samples/T7_EGG.png"



    while True:
        count += 1
        print("Battles done: {}".format(count))

        time.sleep(1.5)

        waitForScreen("PVP_Samples/Fight")
        print("Clicked PVP_Samples/Fight")

        time.sleep(2)

        if pyautogui.locateOnScreen("PVP_Samples/Shield_Yes.png", confidence=0.8):

            (x, y) = pyautogui.position()
            pyautogui.click(pyautogui.locateOnScreen("PVP_Samples/Shield_Yes.png", confidence=0.8))
            print("Clicked PVP_Samples/Shield_Yes")
            pyautogui.moveTo(x, y)

            waitForScreen("PVP_Samples/Start_Battle")
            print("Clicked PVP_Samples/Start_Battle")

            waitForScreen("PVP_Samples/Auto")
            print("Clicked PVP_Samples/Auto")

            waitForScreen("PVP_Samples/Win_Lose")

            if tries > 390:
                waitForScreen("PVP_Samples/Active_Auto")
                print("Clicked PVP_Samples/Active_Auto")

                time.sleep(1)

                (x, y) = pyautogui.position()
                pyautogui.click(858, 75)
                print("Clicked PVP_Samples/Exit")
                pyautogui.moveTo(x, y)

                (x, y) = pyautogui.position()
                pyautogui.click(527, 453)
                print("Clicked PVP_Samples/Yes")
                pyautogui.moveTo(x, y)

            (x, y) = pyautogui.position()
            pyautogui.click(858, 75)
            print("Clicked PVP_Samples/Exit")
            pyautogui.moveTo(x, y)

            time.sleep(3)

            if pyautogui.locateOnScreen("PVP_Samples/Collect.png", confidence=0.8):
                Egg_Outcome = Check_Egg(T1_EGG_C, T2_EGG_C, T3_EGG_C, T4_EGG_C, T5_EGG_C)
                print(Egg_Outcome)                

                if Egg_Outcome == 1:
                    T1_EGG_C += 1
                    print(str(T1_EGG_C) + "xT1")
                if Egg_Outcome == 2:
                    T2_EGG_C += 1
                    print(str(T2_EGG_C) + "xT2")
                if Egg_Outcome == 3:
                    T3_EGG_C += 1
                    print(str(T3_EGG_C) + "xT3")
                if Egg_Outcome == 4:
                    T4_EGG_C += 1
                    print(str(T4_EGG_C) + "xT4")
                if Egg_Outcome == 5:
                    T5_EGG_C += 1
                    print(str(T5_EGG_C) + "xT5")


                (x, y) = pyautogui.position()
                pyautogui.click(pyautogui.locateOnScreen("PVP_Samples/Collect.png", confidence=0.8))
                print("Clicked PVP_Samples/Collect")
                pyautogui.moveTo(x, y)

                time.sleep(0.4)

                waitForScreen("PVP_Samples/Back")
                print("Clicked PVP_Samples/Back")

                waitForScreen("PVP_Samples/Discard")
                print("Clicked PVP_Samples/Discard")

                time.sleep(2)

                points += 5
                wins += 1
                print("Wins: {}, Loses: {}, Points gained: {}".format(wins, loses, points))
            else:
                loses += 1
                print("Wins: {}, Loses: {}, Points gained: {}".format(wins, loses, points))

            Output_Eggs(T1_EGG_C, T2_EGG_C, T3_EGG_C, T4_EGG_C, T5_EGG_C)

        else:
            waitForScreen("PVP_Samples/Start_Battle")
            print("Clicked PVP_Samples/Start_Battle")

            waitForScreen("PVP_Samples/Auto")
            print("Clicked PVP_Samples/Auto")

            waitForScreen("PVP_Samples/Win_Lose")

            if tries > 300:         # Exit Phase
                waitForScreen("PVP_Samples/Active_Auto")
                print("Clicked PVP_Samples/Active_Auto")

                time.sleep(1)

                (x, y) = pyautogui.position()
                pyautogui.click(858, 75)
                print("Clicked PVP_Samples/Exit")
                pyautogui.moveTo(x, y)

                (x, y) = pyautogui.position()
                pyautogui.click(527, 453)
                print("Clicked PVP_Samples/Yes")
                pyautogui.moveTo(x, y)

            print("Clicked PVP_Samples/Win_Lose")

            # Checking EGG

            (x, y) = pyautogui.position()
            pyautogui.click(858, 75)
            print("Clicked PVP_Samples/Exit")
            pyautogui.moveTo(x, y)
            time.sleep(3)

            if pyautogui.locateOnScreen("PVP_Samples/Collect.png", confidence=0.8):
                Egg_Outcome = Check_Egg(T1_EGG_C, T2_EGG_C, T3_EGG_C, T4_EGG_C, T5_EGG_C)
                print(Egg_Outcome)                

                if Egg_Outcome == 1:
                    T1_EGG_C += 1
                    print(str(T1_EGG_C) + "xT1")
                if Egg_Outcome == 2:
                    T2_EGG_C += 1
                    print(str(T2_EGG_C) + "xT2")
                if Egg_Outcome == 3:
                    T3_EGG_C += 1
                    print(str(T3_EGG_C) + "xT3")
                if Egg_Outcome == 4:
                    T4_EGG_C += 1
                    print(str(T4_EGG_C) + "xT4")
                if Egg_Outcome == 5:
                    T5_EGG_C += 1
                    print(str(T5_EGG_C) + "xT5")

                (x, y) = pyautogui.position()
                pyautogui.click(pyautogui.locateOnScreen("PVP_Samples/Collect.png", confidence=0.8))
                print("Clicked PVP_Samples/Collect")
                pyautogui.moveTo(x, y)

                time.sleep(0.4)

                waitForScreen("PVP_Samples/Back")
                print("Clicked PVP_Samples/Back")

                waitForScreen("PVP_Samples/Discard")
                print("Clicked PVP_Samples/Discard")
                time.sleep(2)

                points += 5
                wins += 1
                print("Wins: {}, Loses: {}, Points gained: {}".format(wins, loses, points))
            else:
                loses += 1
                print("Wins: {}, Loses: {}, Points gained: {}".format(wins, loses, points))

            Output_Eggs(T1_EGG_C, T2_EGG_C, T3_EGG_C, T4_EGG_C, T5_EGG_C)

        if pyautogui.locateOnScreen("PVP_Samples/League.png", confidence=0.7):

            (x, y) = pyautogui.position()
            pyautogui.click(pyautogui.locateOnScreen("PVP_Samples/League.png", confidence=0.8))
            pyautogui.moveTo(x, y)

            time.sleep(1)

            (x, y) = pyautogui.position()
            pyautogui.click(326, 115)
            pyautogui.moveTo(x, y)

def Stardust_Dungeon():
    def Dungeon_Repeat():

        waitForScreen("Fight_Stamina")
        time.sleep(1)

        waitForScreen("Stardust_Fight")

        waitForScreen("Auto")

        waitForScreen("Roulette")

        for spins in range(2):
            time.sleep(1)
            pydirectinput.press("up")

        waitForScreen("Roulette_Exit")

        time.sleep(3)

    def Three_Nodes():
        for i in range(3):
            Dungeon_Repeat()

    def One_Node():
        Dungeon_Repeat()


    # Moves the cursor in a position to which it will drag.
    pyautogui.moveTo(668, 356)
    pyautogui.dragRel(-330, 0, 0.2)

    time.sleep(1)


        # Floor 4 Stage

    (x, y) = pyautogui.position()
    pyautogui.click(127, 540)
    print("Clicked on Enter FLOOR 4")
    pyautogui.moveTo(x, y)
    One_Node()

        # Floor 3 Stage

    (x, y) = pyautogui.position()
    pyautogui.click(817, 540)
    print("Clicked on Enter FLOOR 3")
    pyautogui.moveTo(x, y)
    Three_Nodes()

        # Floor 2 Stage

    (x, y) = pyautogui.position()
    pyautogui.click(500, 540)
    print("Clicked on Enter FLOOR 2")
    pyautogui.moveTo(x, y)
    Three_Nodes()

        # Floor 1 Stage

    (x, y) = pyautogui.position()
    pyautogui.click(180, 540)
    print("Clicked on Enter FLOOR 1")
    pyautogui.moveTo(x, y)
    Three_Nodes()

def MonsterWood_AutoThrough():

    MW_ADS_WATCHED = 0
    time.sleep(1)

    while True:
        print("{} ads watched, Next ad!".format(str(MW_ADS_WATCHED)))

        # Looking for MW_PLAY
        tries = 0

        while True:
            if pyautogui.locateOnScreen("MW_Samples/MW_PLAY.png", confidence=0.8):
                time.sleep(0.5)
                coords = pyautogui.locateOnScreen("MW_Samples/MW_PLAY.png", confidence=0.8)


                (x, y) = pyautogui.position()
                pyautogui.click(coords)
                pyautogui.moveTo(x, y)

                time.sleep(1)
                break
            else:
                tries += 1
                print(str(tries))

                if tries == 10:
                    # Refresh stage
                    (x, y) = pyautogui.position()
                    pyautogui.click(858, 74)
                    pyautogui.moveTo(x, y)
                    print("Clicked on MW_Samples/MW_EXIT_MAIN")

                    time.sleep(0.6)

                    (x, y) = pyautogui.position()
                    pyautogui.click(458, 326)
                    pyautogui.moveTo(x, y)
                    print("Clicked on MW_BUILDING")
                    # Successfully clicked on MW_PLAY button, making an ad play.

        while True:
            # Elapsing 35 second between checking.
            print("Waiting for MW_Samples/MW_EXIT button")
            time.sleep(35)

            # NO_EXIT
            if pyautogui.locateOnScreen("MW_Samples/MW_COLLECT.png", confidence=0.8):
                time.sleep(0.5)

                coords = pyautogui.locateOnScreen("MW_Samples/MW_COLLECT.png", confidence=0.8)

                (x, y) = pyautogui.position()
                pyautogui.click(coords)
                pyautogui.moveTo(x, y)
                break

            # Google Play Exit
            if pyautogui.locateOnScreen("MW_Samples/MW_EXIT_GOOGLEPLAY.png", confidence=0.8):
                time.sleep(0.5)

                coords = pyautogui.locateOnScreen("MW_Samples/MW_EXIT_GOOGLEPLAY.png", confidence=0.8)

                (x, y) = pyautogui.position()
                pyautogui.click(coords)
                pyautogui.moveTo(x, y)
                break

            # White Learn More Exit
            if pyautogui.locateOnScreen("MW_Samples/MW_EXIT_WHITE_LEARNMORE.png", confidence=0.8):
                time.sleep(0.5)

                coords = pyautogui.locateOnScreen("MW_Samples/MW_EXIT_WHITE_LEARNMORE.png", confidence=0.8)

                (x, y) = pyautogui.position()
                pyautogui.click(coords)
                pyautogui.moveTo(x, y)
                break

            # Gradient Exit
            if pyautogui.locateOnScreen("MW_Samples/MW_EXIT_GRADIENT.png", confidence=0.8):
                time.sleep(0.5)
                
                coords = pyautogui.locateOnScreen("MW_Samples/MW_EXIT_GRADIENT.png", confidence=0.8)
                
                (x, y) = pyautogui.position()
                pyautogui.click(coords)
                pyautogui.moveTo(x, y)
                break

            else:
                time.sleep(0.5)

                (x, y) = pyautogui.position()
                pydirectinput.press("esc")
                time.sleep(0.4)
                pydirectinput.press("esc")
                pyautogui.moveTo(x, y)

        waitForScreen("MW_Samples/MW_COLLECT")

        MW_ADS_WATCHED += 1

egg_string = "PVP_Samples/T1_EGG.png"

print(egg_string[13])


choice = input(print("""
1. Buy_100_Rare()
2. PvP_AutoThrough()
3. Stardust_Dungeon()
4. MonsterWood_AutoThrough()

>>
"""))

if choice == "1": Buy_100_Rare()
if choice == "2": PvP_AutoThrough()
if choice == "3": Stardust_Dungeon()
if choice == "4": MonsterWood_AutoThrough()



