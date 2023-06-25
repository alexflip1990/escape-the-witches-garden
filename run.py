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
    print("Welcome to Escape the Witche's garden\n")
    print("The rules are simple\n")
    print("It's your job to help Jimmy make the right decisions\n")
    print("And escape the Witche's garden\n")
    print("Please enter your name\n")
    username = ""
    while True:
        username = input("")
        if not username.isalpha():
            print("Sorry numbers can't be accepted")
            continue
        else:
            print("Welcome " + username)
            print("Let's help Jimmy escape the Witches garden!")
            


