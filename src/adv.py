from room import Room, List
from player import Player
from item import Item
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
room['outside'].items =[Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('OUTSIDE', 'placeholder for when I feel more creative')]
room['foyer'].items = [Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('FOYER', 'placeholder for when I feel more creative')]
room['overlook'].items =[Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('OVERLOOK', 'placeholder for when I feel more creative')]
room['narrow'].items = [Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('NARROW', 'placeholder for when I feel more creative')]
room['treasure'].items = [Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('TREASURE', 'placeholder for when I feel more creative')]


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# outside_list = List(room['outside'].items, room['outside'].name)

# print(room['outside'].items)
# print(outside_list)

# for item in room['outside'].items:
#     print(f'\nItem: {item.name.capitalize()}, Item Description: {item.description}\n')



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Players_Gonna_Play', 'outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
def get_and_drop(item_list):
    split_items= []
    get_items = input('Will you get or drop an item? ')
    split_items = get_items.split(' ')
    print(split_items)

    if get_items == 'no':
        return print('Carry on')

    if split_items[0] == 'get' or split_items[0] == 'take':
        item_to_get = split_items[1]
        for item in item_list:
            print(f'ITEM.NAME: {item.name.lower()}')
            print(f'ITEM_TO_GET: {item_to_get.lower()}')
            if item_to_get.lower() == item.name.lower():
                player1.items.append(item)
                split_items = []
                return print(f"{item.name.capitalize()} has been added {len(player1.items)} total!!")
            
        print('You cannot get that which the room does not contain.')

    elif 'drop' in split_items:
        print('DROPPING')
        item_to_drop = split_items[1]
        for item in player1.items:
            # print(f'ITEM.NAME: {item.name}')
            # print(f'ITEM_TO_drop: {item_to_drop}')
            if item_to_drop.lower() == item.name.lower():
                player1.items.remove(item)
                split_items = []
                return print(f"{item.name.capitalize()} has been removed, {len(player1.items)} left!!")
        print('You cannot drop that which you do not have.')

def print_location(room_desc, room_name):
    print(textwrap.fill(f'\n{player1.name} is currently {player1.current_room}. {room_desc} and has {len(player1.items)} items'))
    print(room[room_name].items)
    for item in room[room_name].items:
        print(f'\nItem: {item.name.capitalize()}, Item Description: {item.description}\n')
    get_and_drop(room[room_name].items)
    get_and_drop(room[room_name].items)
    # get_items = input('Will you get or drop an item? ')
    # split_items = get_items.split(' ')

    # if get_items == 'no':
    #     return print('Carry on')

    # if 'get' or 'take' in split_items:
    #     item_to_get = split_items[1]
    #     for item in room[room_name].items:
    #         # print(f'ITEM.NAME: {item.name}')
    #         # print(f'ITEM_TO_GET: {item_to_get}')
    #         if item_to_get.lower() == item.name.lower():
    #             player1.items.append(item)
    #             return print(f"{item.name.capitalize()} has been added!!")
            
    #     print('You cannot get that which the room does not contain.')

    # if 'drop' in split_items:
    #     item_to_drop = split_items[1]
    #     for item in room[room_name].items:
    #         # print(f'ITEM.NAME: {item.name}')
    #         # print(f'ITEM_TO_drop: {item_to_drop}')
    #         if item_to_drop.lower() == item.name.lower():
    #             player1.items.remove(item)
    #             return print(f"{item.name.capitalize()} has been removed!!")
            
        # print('You cannot get that which the room does not contain.')


def print_quit():
    print('\nUntil our stars align again, I bid you farewell traveler')

def print_invalid_direction():
    print('\nTherein lies that which you have not prepared for, please choose a different direction.')

def move_foyer(move):
    if move == 's':
        foyer_move_s = room["foyer"].s_to
        player1.current_room = foyer_move_s.name
        print_location(foyer_move_s.description, "outside")
    elif move == 'e':
        foyer_move_e = room[player1.current_room.lower()].e_to
        player1.current_room = foyer_move_e.name
        print_location(foyer_move_e.description, "narrow")
    elif move == 'n':
        foyer_move_n = room[player1.current_room.lower()].n_to
        player1.current_room = foyer_move_n.name
        print_location(foyer_move_n.description, "overlook")
    elif move == 'w':
        print_invalid_direction()

def move_outlook(move):
    if move == 's':
        overlook_move_s = room["overlook"].s_to
        player1.current_room = overlook_move_s.name
        print_location(overlook_move_s.description,"foyer" )
    else:
        print_invalid_direction()

def move_narrow(move):
    if move == 'w':
        narrow_move_w = room["narrow"].w_to
        player1.current_room = narrow_move_w.name
        print_location(narrow_move_w.description, "foyer")
    elif move == 'n':
        narrow_move_n = room["narrow"].n_to
        player1.current_room = narrow_move_n.name
        print_location(narrow_move_n.description, "treasure")
    else:
        print_invalid_direction()

def move_treasure(move):
    if next_move == 's':
        treasure_move_s = room["treasure"].s_to
        player1.current_room = treasure_move_s.name
        print_location(treasure_move_s.description, "narrow")
    else:
        print_invalid_direction()

while True:
    try:
        print_location(room[player1.current_room].description, "outside")
        first_move = input('\n~~~~> Will you go north, traveler? (Enter n to accept adventure) ')
        if first_move == 'n':
           print('\nSo you choose Adventure.')
           new_room = room[player1.current_room].n_to
           player1.current_room = new_room.name
           print_location(new_room.description, "foyer")
           break
        elif first_move == 'q':
            print_quit()
            break
        else:
            print('\nYou must not deny destiny, the only path forward is North. Accept faith by choosing n for North')
            continue
    except:
        pass



while True:
    try:
        if player1.current_room == 'outside' and first_move == 'q':
            break
        choices = ['n', 's', 'e', 'w']
        next_move = input('\n~~~~> Will you explore or keep moving, traveler?\n~~~~> (Type explore to search for items or enter a direction to keep moving.) ')
        if next_move == 'q':
            print_quit()
            break
        if next_move == 'explore':
            print("I'm exploring!!!")
            continue
        if player1.current_room.lower() == 'foyer' and next_move in choices:
            move_foyer(next_move)

            continue
        if player1.current_room == 'Grand Overlook' and next_move in choices:
            move_outlook(next_move)
            continue
        if player1.current_room == 'Narrow Passage'  and next_move in choices:
            move_narrow(next_move)
            continue
        if player1.current_room == 'Treasure Chamber'  and next_move in choices:
            move_treasure(next_move)
            continue

        if next_move not in choices:
            print(f'\nPerhaps, you are more than we take you for. For now though you may only move in the four cardinal directions: n for North, s for South, e for East, w for West')
            continue
    except:
        pass