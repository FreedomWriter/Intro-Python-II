from room import Room
from player import Player
import textwrap

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
# print(room['outside'].n_to)
# print(room['foyer'].n_to)
# print(room['foyer'].e_to)
# print(room['foyer'].s_to)
# print(room['outside'].s_to)



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('PlayersGonnaPlay', 'outside')
print(player1.current_room)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

while True:
    try:
        print(textwrap.fill(f'{player1.name} is currently {player1.current_room}. {room[player1.current_room].description}'))
        first_move = input('~~~~> Will you go north, traveler? (Enter n to accept adventure) ')
        if first_move == 'n':
           print('So you choose Adventure.')
           new_room = room[player1.current_room].n_to
           player1.current_room = new_room.name
           print(textwrap.fill(f'{player1.name} is currently {player1.current_room}. {new_room.description}'))
           break
        elif first_move == 'q':
            print('Until our stars align again, I bid you farewell traveler')
            break
        else:
            print('You must not deny destiny, the only path forward is North.')
            continue
    except:
        pass



    # # print(f'Ah, so you choose {next_move}')
while True:
    try:
        next_move = input('~~~~> Where next, traveler? ')
        if next_move == 's':
            foyer_move_s = room[player1.current_room.lower()].s_to
            player1.current_room = foyer_move_s.name
            print(textwrap.fill(f'{player1.name} is currently {player1.current_room}. {foyer_move_s.description}'))
            break
        elif next_move == 'e':
            foyer_move_e = room[player1.current_room.lower()].e_to
            player1.current_room = foyer_move_e.name
            print(textwrap.fill(f'{player1.name} is currently {player1.current_room}. {foyer_move_e.description}'))
            break
        elif next_move == 'n':
            foyer_move_n = room[player1.current_room.lower()].n_to
            player1.current_room = foyer_move_n.name
            print(textwrap.fill(f'{player1.name} is currently {player1.current_room}. {foyer_move_n.description}'))
            break
        elif next_move == 'w':
            print('To the west lies, that which you have not prepared for.')
            continue
        elif next_move == 'q':
            print('Until our stars align again, I bid you farewell traveler')
            break
        else:
            print(f'Perhaps, you are more than we take you for. For now though you may only move in the four cardinal directions: n for North, s for South, e for East, w for West')
            continue
    except:
        pass


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#helper function to handle moves
# choice list 