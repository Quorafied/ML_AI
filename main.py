import pyautogui
import pydirectinput
import time
import cv2 as cv

pyautogui.FAILSAFE = False

time.sleep(3)

print(pyautogui.position())
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
    return tries


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

def MonsterWood_AutoThrough2():
    List_EXIT_SINGLE = [
        "MW_Samples/MW_EXIT_SINGLE.png",
        "MW_Samples/MW_EXIT_SINGLE2.png",
        "MW_Samples/MW_EXIT_SINGLE3.png",
        "MW_Samples/MW_EXIT_Single4.png",
        "MW_Samples/MW_EXIT_GOOGLEPLAY.png",
        "MW_Samples/MW_EXIT_WHITE_LEARNMORE.png",
        "MW_Samples/MW_EXIT_GRADIENT.png"
        ]

    def reopenPlayScreen():
        waitForScreen("MW_Samples/MW_PLAYSCREEN_EXIT")
        time.sleep(2)

        (x, y) = pyautogui.position()
        pyautogui.click(464, 291) # Click on MW_BUILDING
        pyautogui.moveTo(x, y)

    def checkDoubleButtonAd():
        if pyautogui.locateOnScreen("MW_Samples/MW_EXIT_DOUBLE.png", confidence=0.8):
            return True
    
    def checkSingleButtonAd():
        while True:
            for exits in List_EXIT_SINGLE:
                if pyautogui.locateOnScreen(exits, confidence=0.8) != None: 
                    return True
                    break
            break

        return False

    def newTabAd():
        (x, y) = pyautogui.position()

        # Click on the frame of the window to activate it.
        pyautogui.click(929, 371)
        time.sleep(1)

        # Click on the Home tab.
        pyautogui.click(204, 26)
        time.sleep(0.4)

        # Click on the Monsters tab.
        pyautogui.click(362, 26)
        pyautogui.moveTo(x, y)

        time.sleep(7)

        pydirectinput.press("esc")

    while True:
        MW_ADS_WATCHED = 0
        Error = False

        print("{} ads watched, next ad!".format(str(MW_ADS_WATCHED)))

        # Click on Play Button or error occurs, fixed in upcoming "while True".
        if waitForScreen("MW_Samples/MW_PLAYBUTTON") == 301:
            Error = True

        while True:
            
            # If the Play Button could not be found in 300 tries, reopens the tab and reloops.
            if Error == True: # Find what type of error before continuing!!
                reopenPlayScreen()
                break
            
            # Wait 35 seconds for an ad to finish, before doing checks.
            time.sleep(33)
            print("Time to checkie checkie")
            
            # Checks if the ad closed itself.
            if pyautogui.locateOnScreen("MW_Samples/MW_COLLECT.png", confidence=0.9):
                (x, y) = pyautogui.position()

                # Click on the frame of the window to activate it.
                pyautogui.click(929, 371)
                time.sleep(1)

                pydirectinput.press("esc")
                pyautogui.moveTo(x, y)
                break

            # Checks if a SingleButton Ad popped up.
            if checkSingleButtonAd() == True:
                print("SINGLE")
                (x, y) = pyautogui.position()

                # Click on the frame of the window to activate it.
                pyautogui.click(929, 371)
                time.sleep(1)

                pydirectinput.press("esc")
                pyautogui.moveTo(x, y)
                break

            # Checks if a DoubleButton Ad popped up.
            if checkDoubleButtonAd() == True:
                print("DOUBLE")
                (x, y) = pyautogui.position()

                # Click on the frame of the window to activate it.
                pyautogui.click(929, 371)
                time.sleep(1)

                pydirectinput.press("esc")
                time.sleep(0.5)
                pydirectinput.press("esc")

                pyautogui.moveTo(x, y)
                break

            else:
                newTabAd()
                break

        # Waiting for the Reward Popup to properly display.
        time.sleep(2) 
        waitForScreen("MW_Samples/MW_COLLECT")

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
if choice == "4": MonsterWood_AutoThrough2()



