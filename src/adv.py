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
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


player_name = input('Welcome!  Please enter your name, fine adventurer!\n')

new_player = Player(player_name, room['outside'])

print(
    f'Welcome, {new_player.name}!  Your journey begins!\n')

user_input = ''

while not user_input == 'q':

    print(
        f'You are currently located in {new_player.current_room.name}.\n')

    user_input = input(
        'Enter a command.  For possible commands type `help`.\n')

    if user_input == 'help':
        print('Enter n, e, w, s to move to a new room.\n')

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
        else:
            print(f'{user_input} is and invalid move.\nPlease enter n, e, s, or w\n')

print('The game has ended!')
