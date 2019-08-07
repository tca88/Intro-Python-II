from room import Room
from player import Player
import textwrap
import sys


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
playerName = input("Please enter your name and let the adventure begin!: ")
p = Player(playerName, room['outside'])
print(f"Welcome, {p.name}! Let's begin the adventure!")

inRoom = True
while inRoom:
    try:
        print(f"You're currently in {p.current_room.name}! Here is what awaits you: {p.current_room.description}")
        userInput = input('Pick a direction to move to next.\n Enter n for North, s for South, e for East or w for West. To quit the game, enter q. ')
        cardinalDirection = userInput
        if cardinalDirection == "q":
            inRoom = False
            print("You've successfully exited the game")
            continue

        if cardinalDirection == 'n' or cardinalDirection == 's' or cardinalDirection == 'e' or cardinalDirection == 'w':
            try:
                if cardinalDirection == 'n':
                    newRoom = p.current_room.n_to
                if cardinalDirection == 's':
                    newRoom = p.current_room.s_to
                if cardinalDirection == 'e':
                    newRoom = p.current_room.e_to
                if cardinalDirection == 'w':
                    newRoom = p.current_room.w_to
                p.current_room = newRoom
                print(f"{p.current_room.name}")
                continue

            except ValueError:
                print("That's not a valid direction. Please try again.")
                continue
    except:
        print(f'Uh oh, looks like {cardinalDirection} is not a valid direction.\nYou will need to restart the game.\n')
        sys.exit(1)
        continue
    
print('The game has ended!')
