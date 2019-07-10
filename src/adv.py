from room import Room
from player import Player
from item import Item

import textwrap

room = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mount beckons'),

    'foyer':    Room('Foyer', '''Dim light filters in from the south. Dusty
passages run north and east.'''),

    'overlook': Room('Grand Overlook', '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.'''),

    'narrow':   Room('Narrow Passage', '''The narrow passage bends here from west
to north. The smell of gold permeates the air.'''),

    'treasure': Room('Treasure Chamber', '''You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.'''),

    'cove': Room('Cove of Echos', '''Welcome to the Cove of Echos, where sound bounces ad infinitum.
Only the most brave enter the Cove of Echos and scream,
but they also never leave.'''),

    'mountain': Room('Mountain of Espers', '''A magical mountain rumored to be full of mana at its core and home of white magic and healing magic.
Some say its magical ponds will turn back the hands of time and
revive the most weary of warriors.'''),

    'meadows': Room('Meadows of Rahnakor', '''The ancient meadows are full of natural medicine and natural spells.
Some say, if you are full of luck,
you may just run into a magical esper that will grant you three wishes.
Listen, carefully, and you might hear their song...
    ''')
}


room['outside'].items = [Item('wand', 'a magic wand of many wonders'), Item(
    'staff', 'the staff of one thousand truths')]
room['foyer'].items = [
    Item('cardboard', 'a pretty crappy item, at least it appears to be.')]
room['overlook'].items = [Item('mana', 'a bottle of mana'), Item(
    'fire', 'a basic fire spell'), Item('ice', 'a basic, but cool ice spell')]
room['narrow'].items = [Item('potion', 'a bottle of an odd, unknown viscous material'), Item(
    'luck', 'the fairy Queen casts the spell of Luck upon yee soul.')]
room['treasure'].items = [Item('goldnugget', 'A gold nugget, pretty self-explanatory'), Item(
    'doom', 'this pretty much just blows up the entire world except for parts of Antartica, and half of Sri Lanka.')]

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['meadows']
room['meadows'].s_to = room['mountain']
room['mountain'].e_to = room['cove']


player_name = input('Welcome!  Please enter your name, fine adventurer!\n')

new_player = Player(player_name, room['outside'])

print(
    f'Welcome, {new_player.name}!  Your journey begins!\n')

user_input = ''

while not user_input == 'q':

    print(
        f'You are currently located in {new_player.current_room.name}.\n')

    current_room_items = new_player.current_room.items
    print('Current room items:')
    for item in current_room_items:
        print(item.name)

    user_input = input(
        'Enter a command.  For possible commands type `help`.\n')

    if user_input == 'help':
        print('Enter n, e, w, s to move to a new room.\nPick up items by using take `item name` or get `item name`\nDrop an item with drop `item name`.\n')
        continue

    split_input = user_input.split(' ')

    if len(split_input) == 2:
        if split_input[0] == 'get' or split_input[0] == 'take':
            room_items = new_player.current_room.items
            for item in room_items:
                if item.name == split_input[1]:
                    new_player.current_room.items.remove(item)
                    new_player.items.append(item)
                    item.on_take()
                    continue
                else:
                    print('The item is not in this room.')

        if split_input[0] == 'drop':
            for item in new_player.items:
                if item.name == split_input[1]:
                    new_player.items.remove(item)
                    new_player.current_room.items.append(item)
                    item.on_drop()
                    continue
                else:
                    print('You can\'t drop something that doesn\'t exist')

    else:
        print(
            f'Please read the following description: {new_player.current_room.description}')

        if user_input == 'n' or user_input == 'e' or user_input == 'w' or user_input == 's':
            try:
                if user_input == 'n':
                    new_room = new_player.current_room.n_to
                if user_input == 'e':
                    new_room = new_player.current_room.e_to
                if user_input == 's':
                    new_room = new_player.current_room.s_to
                if user_input == 'w':
                    new_room = new_player.current_room.w_to
                print(f'You entered the valid move - {user_input}!\n')
                new_player.current_room = new_room

            except:
                print('Move was not valid for current location.\n Try again.\n')
        elif user_input == 'inventory' or user_input == 'i':
            print('This is your current inventory:')
            for item in new_player.items:
                print(item.name)
        else:
            print(f'{user_input} is and invalid move.\nPlease enter n, e, s, or w\n')


print('The game has ended!')
