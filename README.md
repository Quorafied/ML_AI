# Monster Legends AI (Outdated & Discontinued)
# A Monster Legends IR multi-bot
<table>
<tr>
<td>
  A bot that uses image recognition to assist and automate certain aspects of the game, from simple things 
like autoclicking to more advanced, decision making tasks. This is purely for educational purposes and I
do note tolerate cheating in any way, shape or form.
</td>
</tr>
</table>

## Features
The bot comes with a set of actions to complete, in a command line fashion, as of right now. This will
be turned into a gui style program.

### PVP Bot
The bot will do a loop of the following:
- Start a battle and turn the game's Auto action on. (It will battle using the game's built-in AI)
- Confirm a loss or a win.
- If a win, collect the reward and take a note of what rewards have been received as well as the win.
- If a loss, it will also take a note of the loss.
- Before looping again, it will output wins, loses, rewards, battles done.

### AutoClicker
An autoClicker is present so that instead of tapping 100 times to purchase available stock of items,
the program will click 100 times at the location of the cursor, although, click intervals is higher 
due to what is used for the program, pydirectinput clicks.
#### Demo
https://imgur.com/a/wS3Z0Gd

### Monster Wood Ads
The bot is presented with a tool that goes itself through all ads that it is presented to itself during events.
What it does:
- Clicks on the Button to play an Ad.
- Checks for errors and fix any errors, replaying an ad. Otherwise, waits for the ad to end.
- It checks in which way the ad ended, there is 6 ways an ad can end. (Closes itself, double buttons, etc.)
- Takes the check in consideration and acts apropriately, checking for a roulette or rewards and loops through, again.

### Stardust Dungeon
An older feature that was programmed, yet its purpose was removed with the company removing this feature 
from the game. It would go through floors of a dungeon by itself, claming roulette rewards at the same time.
- This is yet to be revamped in the future to accomodate more types of dungeons.

## What was used
- pyautogui and pydirectinput.
- OpenCV for image recognition confidence
- Python 3.8.0+

# Roadmap and Bugs
A list of upcoming changes, bugs to be fixed and the program's Roadmap can be found at:
- https://trello.com/b/UdF8V4Bb/monster-legends-multiai
