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
    cprint("Welcome to Escape the Witche's garden", "magenta", attrs=["bold"])
    print("The rules are simple")
    print("It's your job to help Jimmy make the right decisions")
    print("And escape the Witche's garden")
    print("Please enter your name\n")
    username = ""
    while True:
        username = input("Enter name here: ")
        if username.isdigit():
            print("Sorry sole numbers or empty inputs can't be accepted")
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
    option_1 = "Jimmy escapes the cage and dashes out the door!"
    option_2 = "Help does not come, no one knows where Jimmy is!"
    players_choice = ""
    players_choice = str(input("Which option do you choose, 1 or 2? "))
    if players_choice == "1":
        print(option_1)
        print("\n")
        time.sleep(3)
        witches_garden()
    elif players_choice == "2":
        print(option_2)
        time.sleep(2)
        game_over()
    else:
        print("Please select options 1 or 2")


def witches_garden():
    """
    Second chapter, the witches garden, here the player has 3
    options to choose from. The code will check if an option has
    been choosen and is promted to choose again if an invalid option
    is chosen.
    """
    cprint("Phew, I made it out says Jimmy....but where the heck am I?", "red")
    print("A crow lands on a near tree")
    cprint("SQUACK.... you ok there friend? What's your name?", "cyan")
    cprint("M mm my names Jimmy he replies", "red")
    cprint("SQUACK...Well Jimmy a kid like you has no place in the" +
           "witches garden", "cyan")
    cprint("SQUACK...It's very dangerous here! I could help you escape?\n", "cyan")
    time.sleep(5)
    print("What should Jimmy do?")
    print("Option 1: Follow the crow's path through the garden")
    print("Option 2: Choose his own path")
    print("Option 3: Shout for help!")
    print("\n")
    option_1 = "SQUACK...Follow me Jimmy let's get you outta here!"
    option_2 = "Thanks, but no thanks, I'll find my own way out"
    option_3 = ("You shout for help and woke the witch, tonights special\n"
                "..Jimmy soup!")
    players_choice = ""
    players_choice = str(input("Which option do you choose, 1, 2 or 3? "))
    if players_choice == "1":
        cprint(option_1, "cyan")
        ("\n")
        time.sleep(5)
        crows_path()
    elif players_choice == "2":
        cprint(option_2, "red")
        ("\n")
        time.sleep(5)
        own_path()
    elif players_choice == "3":
        print(option_3)
        time.sleep(2)
        game_over()
    else:
        print("Please select options 1, 2 or 3")


def crows_path():
    """
    Third chapter, the crow's path, the player has chosen to follow
    the crows path, here they are given two options, both options
    are accepted to move to the next chapter, the code will check
    if an option has been chosen and ask the player to choose a valid option.
    """
    print("Jimmy follows the crow into the garden")
    print("After running for a wile, they come to rest")
    cprint("SQUACK...You should drink some water Jimmy" +
          "to keep you hydrated said the crow", "cyan")
    cprint("SQUACK...There's a water fountain over there," +
          "you should drink some?\n", "cyan")
    time.sleep(5)
    print("What should Jimmy do?")
    print("Option 1: Listen to the crow and drink from the fountain")
    print("Option 2: Ignore the crow and keep going")
    print("\n")
    option_1 = "Thanks crow, I feel much better, let's keep going!"
    option_2 = "It's ok, I can go a little longer"
    players_choice = ""
    players_choice = str(input("Which option do you choose, 1 or 2? "))
    ("\n")
    if players_choice == "1":
        cprint(option_1, "red")
        ("\n")
        time.sleep(5)
        candy_bush()
    elif players_choice == "2":
        cprint(option_2, "red")
        ("\n")
        time.sleep(5)
        candy_bush()
    else:
        print("Please select options 1 or 2")


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
    cprint("WOOOOAAAHHHH...Jimmy says, is that..a candy bush!??", "red")
    print("Lushest green leaves and bright coloured candy" +
          "hanging from the vines")
    print("Jimmy moves closer to the candy bush and reaches for the candy")
    cprint("SQUACK...Careful Jimmy I wouldn't eat that candy if I was you", "cyan")
    cprint("SQUACK...It could be spelled by the witch!!!\n", "cyan")
    time.sleep(5)
    print("What should Jimmy do?")
    print("Option 1: Eat the candy from the bush")
    print("Option 2: Listen to the crows warning")
    print("\n")
    option_1 = ("Jimmy eats the candy and starts to choke\n "
                "SQUACK...I told you not to eat it Jimmy says the crow\n "
                "The crow was right, the candy was poisend\n "
                "and poor Jimmy dies")
    option_2 = ("I trust you Mr crow, I shouldn't eat candy\n "
                "from a witches garden!")
    players_choice = ""
    players_choice = str(input("Which option do you choose, 1 or 2? "))
    if players_choice == "1":
        cprint(option_1, "cyan")
        time.sleep(2)
        game_over()
    elif players_choice == "2":
        cprint(option_2, "red")
        time.sleep(5)
        crows_trap()
    else:
        print("Please select options 1 or 2")


def crows_trap():
    """
    Fith chapter, crows trap, the player has followed the crow
    and taken their advice only to find this path leads to a trap,
    there are no options to choose from in this chapter it leads
    to game over
    """
    print("After taking the crows advice and not eating the candy")
    cprint("Jimmy carries on running....I see it Jimmy shouts!", "red")
    cprint("I SEE THE WAY OUT!!..Faster and faster he runs until..", "red")
    cprint("YIKES!! Jimmy yells and falls into a disguised pit", "red")
    cprint("HELP, HELP yells Jimmy to the crow", "red")
    cprint("SQUACK...Pooor Jimmy, you didn't really think I'd help", "cyan")
    cprint("you escape my master now did you?", "cyan")
    cprint("SQUACK...I'll go let her know supper is ready!", "cyan")
    ("\n")
    game_over()


def own_path():
    """
    Sixth chapter, own path, this chapter comes into play
    if the player selects option 2 in the witches garden,
    Jimmy arrives at a river and has 3 options, options 1 and 3
    will lead to death, option 2 will get Jimmy across the river,
    the code will check for a selected option and prompt the player
    to make a decision, a choice has to be made to carry on playing.
    """
    print("Jimmy ignores the crow and makes a run for it")
    print("He arrives at a river where there's a brigde to cross")
    print("Jimmy approaches the bridge but the middle has collapsed")
    cprint("I think i could make that jump Jimmy says", "red")
    print("To the side of the bridge by the rivers edge is a old rowing boat")
    cprint("Or maybe use the boat, although its's badly damaged", "red")
    cprint("Maybe I could swim across, it doesn't look too deep?", "red")
    cprint("NNOOOOOO!!! Jimmy hears the witch scream", "green")
    print("And watches her fly into the night sky cackling away")
    cprint("I best hurry!!!! says Jimmy\n", "red")
    time.sleep(5)
    print("What should Jimmy do?")
    print("Option 1: Jump across the bridge")
    print("Option 2: Use beaten up rowing boat")
    print("Option 3: Swim across the river")
    print("\n")
    option_1 = ("Jimmy jumps but doesn't make it/n "
                "he falls in the river and drowns")
    option_2 = ("Jimmy uses the boat and makes it across,\n "
                "the boat sinks when he\n "
                "gets off..theres no going back now!")
    option_3 = ("Some rivers you swim in, witches rivers you shouldn't,\n"
                "Jimmy is pulled the depths by mystical creatures")
    players_choice = ""
    players_choice = str(input("Which option do you choose, 1, 2 or 3? "))
    if players_choice == "1":
        print(option_1)
        ("\n")
        time.sleep(3)
        game_over()
    elif players_choice == "2":
        print(option_2)
        ("\n")
        time.sleep(5)
        cyclops_battle()
    elif players_choice == "3":
        print(option_3)
        ("\n")
        time.sleep(3)
        game_over()
    else:
        print("Please select options 1, 2 or 3")


def cyclops_battle():
    """
    Seventh chapter, cyclops battle, this chapter comes
    into play once Jimmy makes it safely across the river,
    where he enters some forestry and is confronted by a cyclops.
    The player decides if Jimmy should fit the cyclops or make a run
    for it, fighting the cyclops will result in death.
    The code will check for which option has been selected and prompt
    the player to make a choice
    """
    print("From the river Jimmy runs into a small forest area " +
          "full of overgrowth")
    print("In the center is a clear opening")
    cprint("That looks like a good place to rest says Jimmy", "red")
    print("Jimmy lays down to rest for a moment")
    time.sleep(3)
    print("From the shadows a giant cyclops emerges and spots Jimmy")
    print("It charges towards Jimmy full of rage\n")
    time.sleep(3)
    print("What should Jimmy do?")
    print("Option 1: Use slingshot from backpack to fight the cyclops")
    print("Option 2: RUN, RUN, RUN!!")
    print("\n")
    option_1 = "This isn't David v Goliath! Jimmy gets eaten by the cyclops"
    option_2 = "The cyclops is tooo big to keep up with me through the forest!"
    players_choice = ""
    players_choice = str(input("Which option do you choose, 1 or 2? "))
    if players_choice == "1":
        print(option_1)
        ("\n")
        time.sleep(3)
        game_over()
    elif players_choice == "2":
        cprint(option_2, "red")
        ("\n")
        time.sleep(5)
        escape_garden()
    else:
        print("Please select options 1 or 2")


def escape_garden():
    """
    Eighth chapter, escape garden, this chapter runs if the cyclops
    battle is won, the player has 3 options to choose from, the player
    is prompted to choose an option to complete the game.
    """
    print("Jimmy makes it out of the forest in one piece!")
    cprint("And see's a red door in the distance amongst a wall of hedges, " +
          "is that the exit!? Jimmy says", "red")
    print("Next to the red door is a rabbit hole, " +
          "it looks like it goes under the hedge")
    cprint("I don't know about this, maybe I should use my flash light and " +
          "look for another way out Jimmy says\n", "red")
    time.sleep(5)
    print("What should Jimmy do?")
    print("Option 1: Open the red door and run as fast as you can")
    print("Option 2: Get down and dirty down the rabbit hole")
    print("Option 3: Use flash light to look for another exit")
    option_1 = ("The red door teleports Jimmy right back to the\n " 
                "witches house\n "
                "CACKLE...I knew you'd pick the easy way out,\n "
                "welcome back Jimmy!")
    option_2 = ("Jimmy scrabbles down the hole and\n"
                "comes out the other side safely!\n "
                "Congradulations you made it out of the witches garden!!")
    option_3 = ("Jimmy uses his flash light from his backpack\n "
                "The witch sees the light and swoops down\n "
                "and captures Jimmy!\n "
                "Silly boy you think I wouldn't see your\n "
                "flash light?? CACKLE CACKLE")
    players_choice = ""
    players_choice = str(input("Which option do you choose, 1, 2 or 3? "))
    if players_choice == "1":
        cprint(option_1, "green")
        ("\n")
        time.sleep(3)
        game_over()
    elif players_choice == "2":
        print(option_2)
        ("\n")
        time.sleep(3)
        game_over()
    elif players_choice == "3":
        cprint(option_3, "green")
        ("\n")
        time.sleep(3)
        game_over()
    else:
        print("Please select options 1, 2 or 3")


def game_over():
    """
    This function will run when ever the player dies or
    completes the game and will be asked
    if they would like to play again
    """
    print("GAME OVER!..Would you like to start again? Yes or No? ")
    player_choice = ""
    while True:
        player_choice = str(input("").lower())
        if player_choice == "yes":
            user_name_intro()
        elif player_choice == "no":
            cprint("We hope to play with you again soon!", "magenta", attrs=["bold"])
            exit()
        else:
            print("You must type yes or no")


def main():
    """
    Calls the games functions
    """
    user_name_intro()


main()
