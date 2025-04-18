#%%
import time
#%%
import sys
from time import sleep

words1 = "The figure whispers: 'You do not belong here...'"
words2 = "You see Jonathan tied up, weak but alive!"
words3 = "Jonathan speaks up 'I knew you'd come... let's get out of here!'"
words4 = "Dracula hisses 'Stupid Child. You dare disturb my slumber?'"
words5 = "The text reads 'To defeat the Monster, plunge this stake into its cold heart.'"

for char in words1:
    sleep(0.5)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in words2:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in words3:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in words4:
    sleep(0.3)
    sys.stdout.write(char)
    sys.stdout.flush()

#%%
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

location = "outside_the_castle"
sleep(20)

def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower().strip() == "quit":
        print("Game Over.")
        exit()
    return user_input.lower().strip()

while True:
    if location == "outside_the_castle":
        print()
        print("Looking up you see the tall spires of blackened stone...")
        direction1 = get_input("Do you dare enter the Castle? (yes/no) (type quit to exit) ")
        if direction1 == "yes":
            print("You push against the heavy Doors.")
            time.sleep(4)
            print("Slowly, very slowly...")
            time.sleep(4)
            print("they creak open, revealing a seemingly endless hallway.")
            time.sleep(4)
            print("The torches lining these seemingly vacant halls barely create light nor do they offer any comfort.")
            location = "hallway_downstairs"
        else:
            print("Ending 1")
            time.sleep(1)
            print("You turn around, leaving the Castle and Jonathan behind.")
            time.sleep(1)
            print("Game Over.")
            break

    elif location == "hallway_downstairs":
        print()
        print("You follow the hallway... shadows are dancing along the walls...")
        time.sleep(3)
        print("At the end of the hallway you find a long, winding staircase.")
        direction2 = get_input("Do you head upstairs or downstairs? (up/down/back) (type quit to exit) ")
        if direction2 == "up":
            print("You climb the winding stairs...")
            time.sleep(4)
            print("One Step after the other...")
            time.sleep(4)
            print("Until finally, you arrive. Yet another hallway lies before you.")
            location = "hallway_upstairs"
        elif direction2 == "down":
            print("You descend the winding stairs...")
            time.sleep(4)
            print("You arrive in a gloomy crypt. It lies before you, dark and ominous.")
            location = "crypt"
        elif direction2 == "back":
            location = "outside_the_castle"

    elif location == "hallway_upstairs":
        print()
        print("Six doors line the hallway in front of you... The fourth door is bolted shut with a rusty lock. You hear voices coming from behind the fifth door.")
        time.sleep(4)
        direction3 = get_input("Which room would you like to enter? (1-6) (type 7 to go back) (type quit to exit) ")

        if direction3 == "1":
            print("The room is empty, all you see is a boarded up window")
        elif direction3 == "2":
            print("A hooded figure crouches at the other End of the Room...")
            time.sleep(2)
            print(words1)
            time.sleep(2)
            print("Ending 2")
            print("You were discovered by Kukoul. Your story ends here.")
            print("Game Over.")
            break
        elif direction3 == "3":
            print("Countless rats are scurrying around the room...")
            print("You quickly shut the door.")
        elif direction3 == "4":
            print("You force open the rusted lock")
            time.sleep(2)
            print(words2)
            time.sleep(2)
            print("Jonathan draws to his feet, crossing the room and embracing you.")
            print(words3)
            print("Ending 3")
            print("You escape the castle, Jonathan following behind you.")
            print("You made it. Congratulations!")
            break
        elif direction3 == "5":
            print("A group of young men and women turn to face you...")
            time.sleep(2)
            print("They screech in anger. They are Vampires.")
            print("Ending 4")
            print("The Fledglings attack you and make you their fine meal.")
            print("Game Over.")
            break
        elif direction3 == "6":
            print("The Room is empty, all You see is a boarded up window")
        elif direction3 == "7":
            location = "hallway_downstairs"
        else:
            print("This is not a valid option. Please try again.")

    elif location == "crypt":
        print("You enter the crypt, a catacomb designed to shelter the Undead.")
        time.sleep(2)
        print("Inside this tomb lies none other than... Count Dracula.")
        time.sleep(8)
        direction4 = get_input("What do you do? (open coffin/look around/go back) (type quit to exit) ")

        if direction4 == "open coffin":
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
            print(words4)
            print("Game Over.")
            break
        elif direction4 == "look around":
            print("You look around the room.")
            time.sleep(2)
            print("You find an old leather bag with a wooden stake inside.")
            print(words5)
            print("You can do this.")
            time.sleep(3)
            print("You plunge the stake into Dracula's Chest.")
            print("Ending 6")
            print("The Vampire turns to Dust. You defeated Count Dracula. Congratulations!")
            break
        elif direction4 == "go back":
            location = "hallway_downstairs"
        else:
            print("Invalid choice. Try again.")