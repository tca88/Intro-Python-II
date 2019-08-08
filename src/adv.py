from room import Room
from player import Player
from item import Item
import textwrap
import sys


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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

room['outside'].items = [Item('Crystal-Skull', 'A really cool crystal skull'), Item(
    'A-Rock', 'A cool rock')]
room['foyer'].items = [Item('Cloak-of-Invisibility', 'A cloak that makes people invisible')]
room['overlook'].items = [Item('Vision-Stone', 'A stone that can show you the future'), Item(
    'Infinity-Stone', 'You can live forever with it'), Item('Death-Stone', 'You can kill people with it')]
room['narrow'].items = [Item('A-Vase', 'Does nothing, it is a vase'), Item(
    'A-Feather', 'Just a plain old feather')]
room['treasure'].items = [Item('Gold', 'So much goooold'), Item(
    'Diamond', 'So you can shine bright...like a diamond')]

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
print(f"Welcome, {p.name}! You're currently in {p.current_room.name}.\n Here's what awaits you: {p.current_room.description}.\n Now let's begin the adventure!")
userInput = ''
inRoom = True
while inRoom and not userInput == 'q':
    current_room_items = p.current_room.items
    print(f'You are now in {p.current_room.name}!\n')
    print(f'Here is what awaits you next. Choose your next direction accordingly: {p.current_room.description}. ')
    print('Here are the items in the room you are in: ')
    for item in current_room_items:
        print(item.name)
    userInput = input('Enter n, e, w, s to move to a new room.\nPick up items by using get item-name or take item-name\nDrop an item with drop item-name.\n You can also enter i to see your current inventory.')
    actionInputs = userInput.split(' ')

    if len(actionInputs) == 2:
        if actionInputs[0] == 'get' or actionInputs[0] == 'take':
            roomItems = p.current_room.items
            for item in roomItems:
                if item.name == actionInputs[1]:
                    p.current_room.items.remove(item)
                    p.items.append(item)
                    item.on_take()
                    continue
                else:
                    print('The item is not in this room.')

        if actionInputs[0] == 'drop':
            for item in p.items:
                if item.name == actionInputs[1]:
                    p.items.remove(item)
                    p.current_room.items.append(item)
                    item.on_drop()
                    continue
                else:
                    print('You can\'t drop something that doesn\'t exist')
    else:
        if userInput == 'n' or userInput == 's' or userInput == 'e' or userInput == 'w':
            try:
                if userInput == 'n':
                    newRoom = p.current_room.n_to
                if userInput == 's':
                    newRoom = p.current_room.s_to
                if userInput == 'e':
                    newRoom = p.current_room.e_to
                if userInput == 'w':
                    newRoom = p.current_room.w_to
                p.current_room = newRoom
                continue
            except:
                print(f'Uh oh, looks like {userInput} is not a valid direction.\nYou will need to restart the game.\n')
                sys.exit(1)
                continue
        
        elif userInput == 'i':
            print('This is your current inventory:')
            for item in p.items:
                print(item.name)
        
        elif actionInputs[0] == 'get':
            roomItems = p.current_room.items
            for item in roomItems:
                if item.name == actionInputs[1]:
                    p.current_room.items.remove(item)
                    p.items.append(item)
                    item.on_take()
                    continue
                else:
                    print('The item is not in this room.')

        elif actionInputs[0] == 'drop':
            for item in p.items:
                if item.name == actionInputs[1]:
                    p.items.remove(item)
                    p.current_room.items.append(item)
                    item.on_drop()
                    continue
                else:
                    print('Looks like this item does not exist)
        else:
            print(f'{userInput} is an invalid move.\nPlease enter n, e, s, or w\n')
    
print('Game Over!')
