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
    print("And a scary looking witch who appears to be asleep")
    print("To his right he can see a key, it's within arms reach!\n")
    time.sleep(5)
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
            print("\n")
            time.sleep(3)
            witches_garden()
        elif players_choice == options[1]:
            print("Help does not come, no one knows where Jimmy is!")
            game_over()


def witches_garden():
    """
    Second chapter, the witches garden, here the player has 3 
    options to choose from. The code will check if an option has
    been choosen and is promted to choose again if an invalid option
    is chosen.
    """
    print("Phew, I made it out says Jimmy....but where the heck am I?")
    print("A crow lands on a near tree")
    print("SQUACK.... you ok there friend? What's your name?")
    print("M mm my names Jimmy he replies")
    print("SQUACK...Well Jimmy a kid like you has no place in the witches garden")
    print("SQUACK...It's very dangerous here! I could help you escape?\n")
    time.sleep(5)
    print("What should Jimmy do?")
    print("Option 1: Follow the crow's path through the garden")
    print("Option 2: Choose his own path")
    print("Option 3: Shout for help!")
    print("\n")
    options = ["1", "2", "3"]
    players_choice = ""
    while players_choice not in options:
        players_choice = str(input("Which option do you choose, 1, 2 or 3?"))
        if players_choice == options[0]:
            print("SQUACK...Follow me Jimmy let's get you outta here!")
        elif players_choice == options[1]:
            print("Thanks, but no thanks, I'll find my own way out")
        elif players_choice == options[2]:
            print("You shouted for help and woke the witch, tonights special is Jimmy soup!")
            game_over()


def crows_path():
    """
    Third chapter, the crow's path, the player has chosen to follow
    the crows path, here they are given two options, both options
    are accepted to move to the next chapter, the code will check
    if an option has been chosen and ask the player to choose an option.
    """
    print("Jimmy follows the crow into the garden")
    print("After running for a wile, they come to rest")
    print("SQUACK...You should drink some water Jimmy to keep you hydrated said the crow")
    print("SQUACK...There's a water fountain over there, you should drink some?")
    time.sleep(5)
    print("What should Jimmy do?")
    print("Option 1: Listen to the crow and drink from the fountain")
    print("Option 2: Ignore the crow and keep going")
    print("\n")
    options = ["1", "2"]
    players_choice = ""
    while players_choice not in options:
        players_choice = str(input("Which option do you choose, 1 or 2?"))
        if players_choice == options[0]:
            print("Thanks crow, I feel much better, let's keep going!")
        elif players_choice == options[1]:
            print("It's ok, I can go a little longer")


def candy_bush():
    """
    Fourth chapter, candy bush, the player continues along the crows path
    and comes across a bush with candy growing out of it, the player
    has to choose if they should eat the candy or listen to the crows
    warning, if they eat the candy Jimmy is poisend and the game ends.
    """
    print("Deeper and deeper into the garden they go")
    print("Jimmy checking his surroundings for a way out")
    print("Then Jimmy comes to a grinding holt")
    print("WOOOOAAAHHHH...Jimmy says, is that..a candy bush!??")
    print("Lushest green leaves and bright coloured candy hanging from the vines")
    print("Jimmy moves closer to the candy bush and reaches for the candy")
    print("SQUACK...Careful Jimmy I wouldn't eat that candy if I was you")
    print("SQUACK...It could be spelled by the witch!!!")
    time.sleep(5)
    print("What should Jimmy do?")
    print("Option 1: Eat the candy from the bush")
    print("Option 2: Listen to the crows warning")
    print("\n")
    options = ["1", "2"]
    players_choice = ""
    while players_choice not in options:
        players_choice = str(input("Which option do you choose, 1 or 2?"))
        if players_choice == options[0]:
            print("Jimmy eats the candy and starts to choke")
            print("SQUACK...I told you not to eat it Jimmy says the crow")
            time.sleep(2)
            print("The crow was right, the candy was poisend and poor Jimmy dies")
            game_over()
        elif players_choice == options[1]:
            print("I trust you Mr crow, I shouldn't eat candy from a witches garden!")


def crows_trap():
    """
    Fith chapter, crows trap, the player has followed the crow
    and taken their advice only to find this path leads to a trap,
    there are no options to choose from in this chapter it leads
    to game over
    """
    print("After taking the crows advice and not eating the candy")
    print("Jimmy carries on running....I see it Jimmy shouts!")
    print("I SEE THE WAY OUT!!..Faster and faster he runs until..")
    print("YIKES!! Jimmy yells and falls into a disguised pit")
    print("HELP, HELP yells Jimmy to the crow")
    print("SQUACK...Pooor Jimmy, you didn't really think I'd help")
    print("you escape my master now did you?")
    print("SQUACK...I'll go let her know supper is ready!")
    game_over()


    



user_name_intro()
witches_house()
witches_garden()
crows_path()
candy_bush()
game_over()
            


