import random
import json
from Enemies import *
from Room import *
from Player import *


# If True, avoid death scene
deathException = False
roomsTraveled = 0
print("Welcome to some random text based game thing. Please proceed by creating your character: ")

def newPlayer():
    tempname = input("Enter the name of the character: ").capitalize()
    tempgender = input("Enter the gender of your character: ").capitalize()
    temprace = input("Enter the race of your character [Human/Elf/Dwarf/Rock] : ").capitalize()
    if(temprace == "Human"):
        player1 = Player(tempname, 100, tempgender, temprace, 5, 3, 0)
    elif(temprace == "Elf"):
        player1 = Player(tempname, 70, tempgender, temprace, 4, 1, 0)
    elif (temprace == "Dwarf"):
        player1 = Player(tempname, 150, tempgender, temprace, 6, 4, 0)
    elif (temprace == "Rock"):
        player1 = Player(tempname, 1000, tempgender, temprace, 100, 100, 0)
    else:
        print("You've named some unknown race. Surely, you must've meant Aquatic Sponge. From hereon, you'll be identified as an Aquatic Sponge")
        player1 = Player(tempname, 1, tempgender, "Aquatic Sponge", 1, 1, 0)
    return player1



def startStringGen():
    """    Pre-Game Phase    """
    temp = random.randint(0, 4)
    if (temp == 0):
        return(f"\nWith no general plan of attack, {player1.name} begins running off into the dungeon.")
    elif (temp == 1):
        return(f"\nHungry for violence, death, and perhaps a nice side of fries, {player1.name} enters the dungeon.")
    elif (temp == 2):
        return(f"\nOut of pure boredom, {player1.name} performs the electric slide to the dungeon.")
    elif (temp == 3):
        return(f"\n{player1.name} doesn't really want to go to the dungeon, but goes anyway because you said so. *sigh*")
    elif (temp == 4):
        return(
            f"\n{player1.name} is all for risking {gen2} life for some random treasure that might not even possibly exist"
            f" within the treacherous dungeon, and heads right on in.")


def hurtStringGen():
    temp = random.randint(0,10)
    if(temp == 0):
        return f"{player1.name} talks crap about {gen4}. That kinda hurt."
    elif(temp == 1):
        return f"{player1.name} trips {gen4} into a brush of poison ivy and discarded needles. That kinda hurt."
    elif(temp == 2):
        return f"{player1.name} messages {gen2} friends, asking if they wanna hang out. No one responds. That kinda hurt."
    elif(temp == 3):
        return f"{player1.name} forgot to breathe for a couple minutes. That kinda hurt."
    elif (temp == 4):
        return f"{player1.name} runs the player1.hurt(10+player1.atk-player1.defe) method. That kinda hurt"
    elif (temp == 5):
        return f"{player1.name} stretches a bit too vigorously and sprains {gen2} shoulder badly. That kinda hurt."
    elif (temp == 6):
        return f"{player1.name} suplexes {gen4} against the floor."
    elif (temp == 7):
        return f"{player1.name} sneezes incorrectly, damaging {gen2} spinal cord in the process. That kinda hurt."
    elif (temp == 8):
        return f"A random person passes by and laughs at {player1.name}'s appearance. That kinda hurt."
    elif (temp == 9):
        return f"{player1.name} proceeds to take a drink of water, but forgets how and nearly drowns. That kinda hurt."
    elif (temp == 10):
        return f"{player1.name} stretches a bit too vigorously and sprains {gen2} shoulder badly. That kinda hurt."


def death():
    if(deathException == False):
        print(f"It looks like {player1.name} couldn't withstand the dangers of this journey.")
        print("                 ______")
        print("           _____/      \\\\_____")
        print("          |  _     ___   _   ||")
        print("          | | \     |   | \  ||")
        print("          | |  |    |   |  | ||")
        print("          | |_/     |   |_/  ||")
        print("          | | \     |   |    ||")
        print("          | |  \    |   |    ||")
        print("          | |   \. _|_. | .  ||")
        print("          |                  ||")
        print("          |                  ||")
        print("          |                  ||")
        print("  *       | *   **    * **   |**      **\n")
        print(f"You've scored {player1.score} points during this epic journey.")
        if(roomsTraveled == 1):
            print(f"You were able to traverse {roomsTraveled} room.")
        else:
            print(f"You were able to traverse {roomsTraveled} rooms.")
        exit(0)
"""
Global Flags
"""



#Load all rooms into List of Rooms
print("Loading rooms...")
allLoadedRooms = []
allLoadedEnemies = []

try:
    with open('rooms.json', 'r') as f:
        rooms_list = json.load(f)

    for rooms in rooms_list:
        tempTitle = rooms['title']
        tempDesc = rooms['description']
        tempCanExit = rooms['canExit']
        tempRoom = Room(tempTitle, tempDesc, 100, 0, 0, 0, tempCanExit)
        allLoadedRooms.append(tempRoom)

    print("Loading enemies...")
    with open('enemies.json', 'r') as f:
        enemies_list = json.load(f)

    for enemies in enemies_list:
        tempName = enemies['name']
        tempDesc = enemies['description']
        tempHP = enemies['hp']
        tempAtk = enemies['atk']
        tempDefe = enemies['defe']
        tempEnemy = Enemies(tempName, tempDesc, tempHP, tempAtk, tempDefe)
        allLoadedEnemies.append(tempEnemy)

except FileNotFoundError:
    print("JSON cannot be found...nothing exists!!! ARGGGHHHH")
    print("*Universe vanishes*")
    exit(1)


except json.decoder.JSONDecodeError:
    print("JSON has a funky format...therefore...nothing exists!!! ARGGGHHHH")
    print("*Universe vanishes*")
    exit(1)


print(f"{len(allLoadedRooms)} rooms were loaded successfully.")
print(f"{len(allLoadedEnemies)} enemies were loaded successfully.")

""" 

Test if rooms loaded successfully from JSON

for rooms in allLoadedRooms:
    print(rooms)
    
"""


while(True):
    player1 = newPlayer()
    print(player1)

    if(player1 != None):
        break

if(player1.gender == "Male"):
    gen1 = "he"
    gen2 = "his"
    gen3 = "him"
    gen4 = "himself"

elif(player1.gender == "Female"):
    gen1 = "she"
    gen2 = "her"
    gen3 = "her"
    gen4 = "herself"
else:
    gen1 = gen2 = gen3 = "it"
    gen4 = "itself"

if(player1.luck == 0):
    print(f"{player1.name} takes a step towards the dungeon.")
    print(f"Due to {gen2} abysmal luck, {player1.name} critically trips over a rock and rolls off a cliff.")
    player1.hurt(100000)
    death()

elif(player1.luck == 10):
    print(f"{player1.name} takes a step towards the dungeon.")
    print(f"Due to {gen2} incredible luck, the dungeon spews out geysers of money and treasure to {player1.name}.")
    print("Your quest is complete!")
    exit(0)

print(startStringGen())


"""
Game Loop
"""
allRooms = []
visitedIndex = []

while(len(visitedIndex) != len(allLoadedRooms)):
# List of Room objects for backtracking purposes?
    if(len(allRooms) == 0):
        tempNum = 0
        visitedIndex.append(tempNum)
    else:
        while(True):
            tempNum = random.randint(1, len(allLoadedRooms)-1)
            if tempNum not in visitedIndex:
                visitedIndex.append(tempNum)
                break


    currentRoom = allLoadedRooms[tempNum]
    allRooms.append(currentRoom)
    roomsTraveled = len(allRooms)
    exitNow = False
    print(currentRoom)
    while(exitNow == False):
        if (player1.hp <= 0):
            death()
        temp = input(f"{player1.hp}/{player1.maxhp} HP > ").lower()
        if(temp == "look"):
            print(currentRoom)
        elif(temp == "suicide"):
            print(f"{player1.name} has frankly gotten tired with this whole ordeal.")
            player1.hurt(10000)
        elif(temp == "hurt self"):
            print(hurtStringGen())
            player1.hurt(10+player1.atk-player1.defe)
        elif(temp == "cheat"):
            print("You can now exit")
            currentRoom.canExit = True
        elif(temp == "history"):
            print("You've been to the following rooms: ")
            tempNum = 1
            for rooms in allRooms:
                print(f"{tempNum}.) {rooms.title}")
                tempNum += 1
        elif(temp == "next"):
            print(currentRoom.canExit)
            if(currentRoom.canExit == "False"):
                print("With the current situation at hand, you cannot advance just yet...")
            else:
                print("Moving on to the next room...")
                exitNow = True

        else:
            print(f"{player1.name} doesn't really understand what you're trying to tell {gen3}.")


print("You've reached the end of the dungeon!")
exit(0)

"""
# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)
"""
