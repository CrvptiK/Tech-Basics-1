# %%
# As a personal reference, this is the amount of hours spent here: 2,5
# lets start by importing what we need

import sys
import time
from time import sleep

# following this, lets define our constants, these stay the same the entire time so let's make them global

# delays

DELAY_WORDS1 = 0.5
DELAY_WORDS2 = 0.2
DELAY_WORDS3 = 0.1
DELAY_WORDS4 = 0.3
INTRO_DELAY = 20

# and dialogue

WORDS1 = "The figure whispers: 'You do not belong here...'"
WORDS2 = "You see Jonathan tied up, weak but alive!"
WORDS3 = "Jonathan speaks up 'I knew you'd come... let's get out of here!'"
WORDS4 = "Dracula hisses 'Stupid Child. You dare disturb my slumber?'"
WORDS5 = "The text reads 'To defeat the Monster, plunge this stake into its cold heart.'"


# with a bit of help from Google I created the following function, which can be used to insert text delays in the next steps of our coding

def print_with_delay(text, delay):
    for char in text:
        sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()


# now let's create a function to handle user input, including the exit function and make sure capitalization is irrelevant

def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower().strip() == "quit":
        print("Game Over.")
        exit()
    return user_input.lower().strip()


# let's copy in the original code and replace what we can with our previously defined functions
# also lets define this game as the main function and make sure it only starts to run when it is being called as the main function

def main():
    location = "outside_the_castle"

    # this is the game intro, any run of it will start with this

    print('''
One late Evening You approach a tall dark Castle in the Depths of Transylvania.
A Storm is brewing in the Distance, the Static palpable in the Air. Rain is already pouring all around You.
But you are here for a very good Reason.
                                         |
                                        : :
                                       |   |
                                     .|   .:|.
                                     |       |
                           .|       .:     .::.       |.
                           | |      |:.       |      | |
                          .| |.    |         .:|    .| |.
                 :     .  |   |__-'             '-__|   |     .     :
                |.     . .|               .:..          |.   .:    .|
               . |.  .: :|      :..       .:              |:. .   .| .
              .:  :'   .                          ..:'   :. .:   .:' :.
              | :.      :.   ::...                         :.  '  '   |
               :.        .:                 ..::   ..:.   :.   .    .:
                |---_.:-.|      ..    _--__-        :. .:  :.--__:._|
                | :..   .. ..:.      :'     ';  :..      ..|    ..: |
                |        :          | :..     |            :  .:    |
                 :     :.|        .:|         :          .:|  :.  ..:
                 .:      |   .:.    :     ..:''      .:.  .|:.     :
                :      |-|:.. .: ;,.'':.      |'..:.  .:;.. :.     .:
               ,:__---__.::__ :.__:.'         ':.__:..._::'|__-- ..:|.
   ...::..  .:(_____::...__)   .._--::--__--''..--___     (__..:..__..):. ...:::...

You are here to save your friend, Jonathan. He has not answered your letters for so long, something must have happened!
The people of the village nearby told you about this Castle and you are certain Jonathan is here.
''')

    sleep(INTRO_DELAY)

    # now lets get the first user input, giving the player their first choice to make

    while True:
        if location == "outside_the_castle":
            print()
            print("Looking up you see the tall spires of blackened stone...")
            answer1 = get_input("Do you dare enter the Castle? (yes/no) (type quit to exit) ")
            if answer1 == "yes":
                print("You push against the heavy Doors.")
                time.sleep(4)
                print("Slowly, very slowly...")
                time.sleep(4)
                print("they creak open, revealing a seemingly endless hallway.")
                time.sleep(4)
                print(
                    "The torches lining these seemingly vacant halls barely create light nor do they offer any comfort.")
                location = "hallway_downstairs"

            # type in anything but "yes" and the game will end here

            else:
                print("Ending 1")
                time.sleep(1)
                print("You turn around, leaving the Castle and Jonathan behind.")
                time.sleep(1)
                print("Game Over.")
                break

        # the game can of course end here, but long as the player enters the castle, we shall move on and give them another choice to make
        # either heading upstairs or downstairs

        elif location == "hallway_downstairs":
            print()
            print("You follow the hallway... shadows are dancing along the walls...")
            time.sleep(3)
            print("At the end of the hallway you find a long, winding staircase.")
            answer2 = get_input("Do you head upstairs or downstairs? (up/down/back) (type quit to exit) ")
            if answer2 == "up":
                print("You climb the winding stairs...")
                time.sleep(4)
                print("One Step after the other...")
                time.sleep(4)
                print("Until finally, you arrive. Yet another hallway lies before you.")
                location = "hallway_upstairs"
            elif answer2 == "down":
                print("You descend the winding stairs...")
                time.sleep(4)
                print("You arrive in a gloomy crypt. It lies before you, dark and ominous.")
                location = "crypt"
            elif answer2 == "back":
                location = "outside_the_castle"
            else:
                print("This option does not exist. Please try again.")

        # if they choose to go upstairs, this block will run

        elif location == "hallway_upstairs":
            print()
            print(
                "Six doors line the hallway in front of you... The fourth door is bolted shut with a rusty lock. You hear voices coming from behind the fifth door.")
            time.sleep(4)
            answer3 = get_input("Which room would you like to enter? (1-6) (type 7 to go back) (type quit to exit) ")
            if answer3 == "1":
                print("The room is empty, all you see is a boarded up window")
            elif answer3 == "2":
                print("A hooded figure crouches at the other End of the Room...")
                time.sleep(2)
                print_with_delay(WORDS1, DELAY_WORDS1)
                time.sleep(2)
                print("Ending 2")
                print("You were discovered by Kukoul. Your story ends here.")
                print("Game Over.")
                break
            elif answer3 == "3":
                print("Countless rats are scurrying around the room...")
                print("You quickly shut the door.")
            elif answer3 == "4":
                print("You force open the rusted lock")
                time.sleep(2)
                print_with_delay(WORDS2, DELAY_WORDS2)
                time.sleep(2)
                print("Jonathan draws to his feet, crossing the room and embracing you.")
                print_with_delay(WORDS3, DELAY_WORDS3)
                print("Ending 3")
                print("You escape the castle, Jonathan following behind you.")
                print("You made it. Congratulations!")
                break
            elif answer3 == "5":
                print("A group of young men and women turn to face you...")
                time.sleep(2)
                print("They screech in anger. They are Vampires.")
                print("Ending 4")
                print("The Fledglings attack you and make you their fine meal.")
                print("Game Over.")
                break
            elif answer3 == "6":
                print("The Room is empty, all You see is a boarded up window")
            elif answer3 == "7":
                location = "hallway_downstairs"
            else:
                print("This is not a valid option. Please try again.")

        # and if they go down, then the following block is run

        elif location == "crypt":
            print("You enter the crypt, a catacomb designed to shelter the Undead.")
            time.sleep(2)
            print("Inside this tomb lies none other than... Count Dracula.")
            time.sleep(8)
            answer4 = get_input("What do you do? (open coffin/look around/go back) (type quit to exit) ")
            if answer4 == "open coffin":
                print("You push open the heavy lid of Dracula's coffin...")
                time.sleep(3)
                print("Dracula awakens...")
                time.sleep(3)
                print("""
                ********************************************************************************
                *****************************###########*#######********************************
                *************************#############******##########**************************
                **********************############************##########************************
                ********************################**###*******#########***********************
                *******************###########********#*****###############*********************
                ******************###########*###**###########****##########********************
                ****************##*##########################################*******************
                ***************#**############################################******************
                **************#**#############********####******###############*****************
                *************###############****#####****######*****############****************
                *************##############***########****#*#####****###########****************
                ************#*##############*#######*##**#*#*#####****###########***************
                ************#############*############***#**#*#####***###########***************
                ***********################*#########******##*********#######*####**************
                ***********################*+++=---------------=+++******####**####*************
                ***********###########**###*++------------------=++*******###**###**************
                ++++++++++*##########**####+++--------====-------=+********##**###**************
                ++++++++++*#########**#####*+=--------=+==--==---=+*#***#******#####************
                ++++++++++*#####*##***##*##+=------==--======----=+*#***#####*#######***********
                +++++++++*######*#***##***###**=----=-=-=------=*##*##***####*######************
                ++++++++*#######****##*****+=-=**=-=-+-++=+*==*#==++###**###*########*#*********
                ++++++++########***###*****+-==-=***#*+=-=***+=+==+**##**###*#########***+++++++
                +++++++########****##*****+++===----+++=-++-----===+*##***#*#*#########**+++++++
                ++++++#########***###*****++==-------++=-++--------=+*#***#*#*###############***
                +++++*###########*####**#+=---------=++=-+++--------++#*######################**
                ++***####################++--------=+++=-+++--------=+########################**
                **#######################*++=------=+++=-+++-------=++*#######################**
                ##########################++++-----=+++=-+++------++++*#######################**
                ##########################*+++=-----++++-+++------++++*#######################**
                ##########################*+++=------+*+++*=-----=++++########################**
                ##########################*+++=--=*###########*+-=+++*#####################*****
                ##########################*+++++******++++++++++=++++###############*##*********
                **########################+++++-----------------=++++############*#*#**########*
                ***######################*+*++++=++++**++**+++++++++*###############*###########
                #****###############***###+=+++=-==-----*----=+++++++###########################
                ###***##############***###++++*+==+----*#+----==+*+++*###*######################
                #####**#############*#####+=++++**##*=*###++*#+++++==*#*#*######################
                ######**#################*+--===++############*++==--*#*#**#####################
                ########**###############**----***+*#########+**+---**#*#**#####################
                #########**##############***=*****############****++**#*#*######################
                ##########***#############**********########**********#########*################
                #############*###############*********#####*********##########*#################
                ###############################*******####*******############*######***++#####**
                +**##############################******###******#############*#####*+++++*######
                ###******##########################****###*****###################*+*=+++*######
                ###################################*****#*****########*####*###*****+===*#######
                ############################################*#########+===+#+***################
                +++**********#######################################=====++=*###################
                ***************************************#############*++==+=*#######****#########
                #####################################################+=+*=*##**********#########
                ############################################################************########
                ###############################################################********#########
                """)
                time.sleep(6)
                print("Ending 5")
                print_with_delay(WORDS4, DELAY_WORDS4)
                print("Game Over.")
                break
            elif answer4 == "look around":
                print("You look around the room.")
                time.sleep(2)
                print("You find an old leather bag with a wooden stake inside.")
                print(WORDS5)
                print("You can do this.")
                time.sleep(3)
                print("You plunge the stake into Dracula's Chest.")
                print("Ending 6")
                print("The Vampire turns to Dust. You defeated Count Dracula. Congratulations!")
                break
            elif answer4 == "go back":
                location = "hallway_downstairs"
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

# due to the many different options for the player, one can not define many overarching functions for the main code, at least as far as I understand.
# I hope my comments were helpful in understanding this code, and you enjoyed checking it out
# I will test this one last time, to check if everything is in order and then I'll head out
# let's quickly reformat the code via ctrl+alt+L as a last little step
