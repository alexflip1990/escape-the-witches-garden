""" Import libraries for game """
import sys
from termcolor import colored, cprint
import random
import time

def user_name_intro():
    """
     The introduction section, this section explains what the rules for
     the game are and asks the player to input their name whilst running
     a while loop to ensure players name is alphabetical.
    """
    print("Welcome to Escape the Witche's garden")
    print("The rules are simple")
    print("It's your job to help Jimmy make the right decisions")
    print("And escape the Witche's garden")
    print("Please enter your name\n")
    username = ""
    while True:
        username = input("")
        if not username.isalpha():
            print("Sorry numbers can't be accepted")
            continue
        else:
            print("\n")
            print("Welcome " + username)
            print("Let's help Jimmy escape the Witches garden!")
            print("\n")
            witches_house()


def witches_house():
    """
    First chapter, the witches house, here the player is asked
    to make a choice between two options, depending on which option
    they choose will result in a different outcome. The code checks
    which option has been selected and if an invalid option has 
    been chosen, will ask the player to select again.
    """
    print("From a deep sleep Jimmy begins to open his eyes")
    print("To discover he is trapped in a cage suspended from a beam")
    print("With no memory of how he got here he begins to panic")
    print("He looks around and see's a cauldron filled with potion")
    print("And scary looking witch who appears to be asleep")
    print("To his right he can see a key, it's within arms reach!\n")
    time.sleep(3)
    print("What do you do?")
    print("Option 1: Reach for the key and escape the cage")
    print("Option 2: Stay in the cage and hope help comes")
    print("\n")
    options = ["1", "2"]
    players_choice = ""
    while players_choice not in options:
        players_choice = str(input("Which option do you choose, 1 or 2?"))
        if players_choice == options[0]:
            print("Jimmy escapes the cage and dashes out the door!")
        elif players_choice == options[1]:
            print("Help does not come, no one knows where Jimmy is!")
            game_over()
    



user_name_intro()
witches_house()
game_over()
            


