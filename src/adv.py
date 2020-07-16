# from room import Room
# from player import Player
# from item import Item
# import textwrap

# # Declare all the rooms
# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# # Link rooms together
# room['outside'].items =[Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('OUTSIDE', 'placeholder for when I feel more creative')]
# room['foyer'].items = [Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('FOYER', 'placeholder for when I feel more creative')]
# room['overlook'].items =[Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('OVERLOOK', 'placeholder for when I feel more creative')]
# room['narrow'].items = [Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('NARROW', 'placeholder for when I feel more creative')]
# room['treasure'].items = [Item('torch', 'The torch is lit, though the cave seems to have been undisturbed for an eternity'), Item('TREASURE', 'placeholder for when I feel more creative')]

# # Establish routes
# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# # Instantiate Player class
# player1 = Player('Players_Gonna_Play', room['outside'].name)

# def get_and_drop(room):
#     print("I'M IN GET_AND_DROP")
#     print(f"ROOM: {room}")
#     get_items = input('Will you get or drop an item? ')
#     split_items = get_items.split(' ')

#     if get_items == 'no':
#         return print('Carry on')

#     if split_items[0] == 'get' or split_items[0] == 'take':
#         item_to_get = split_items[1]
#         for item in room.items:
#             if item_to_get.lower() == item.name.lower():
#                 player1.items.append(item)
#                 room.on_take(item)
#                 split_items = []
#                 return print(f"You have {len(player1.items)} items, {len(room.items)} left in {player1.current_room}!!")
            
#         return print('You cannot get that which the room does not contain.')

#     elif split_items[0] =='drop':
#         item_to_drop = split_items[1]
#         for item in player1.items:
#             if item_to_drop.lower() == item.name.lower():
#                 player1.items.remove(item)
#                 room.on_drop(item)
#                 split_items = []
#                 return print(f"You have {len(player1.items)} items, {len(room.items)} left in {player1.current_room}!!")
#         return print('You cannot drop that which you do not have.')

# def print_location(room_desc, room_name):
#     print(textwrap.fill(f'\n{player1.name} is currently {player1.current_room}. {room_desc} and has {len(player1.items)} items'))
#     for item in room[room_name].items:
#         print(f'\nItem: {item.name.capitalize()}, Item Description: {item.description}\n')

# def print_quit():
#     print('\nUntil our stars align again, I bid you farewell traveler')

# def print_invalid_direction():
#     print('\nTherein lies that which you have not prepared for, please choose a different direction.')

# def print_player_inventory():
#     if len(player1.items) < 1:
#         print('Inventory Empty')
#     else:

#         print_player_inventory()

# def move_foyer(move):
#     if move == 's':
#         foyer_move_s = room["foyer"].s_to
#         player1.current_room = foyer_move_s.name
#         print_location(foyer_move_s.description, "outside")
#     elif move == 'e':
#         foyer_move_e = room[player1.current_room.lower()].e_to
#         player1.current_room = foyer_move_e.name
#         print_location(foyer_move_e.description, "narrow")
#     elif move == 'n':
#         foyer_move_n = room[player1.current_room.lower()].n_to
#         player1.current_room = foyer_move_n.name
#         print_location(foyer_move_n.description, "overlook")
#     elif move == 'i':
#         get_and_drop(room['foyer'])
#     elif move != 's' or 'e' or 'n' or 'i':
#         print_invalid_direction()

# def move_overlook(move):
#     if move == 's':
#         overlook_move_s = room["overlook"].s_to
#         player1.current_room = overlook_move_s.name
#         print_location(overlook_move_s.description,"foyer" )
#     elif move == 'i':
#         get_and_drop(room['overlook'])
#     elif move != 's' or 'i':
#         print_invalid_direction()

# def move_narrow(move):
#     if move == 'w':
#         narrow_move_w = room["narrow"].w_to
#         player1.current_room = narrow_move_w.name
#         print_location(narrow_move_w.description, "foyer")
#     elif move == 'n':
#         narrow_move_n = room["narrow"].n_to
#         player1.current_room = narrow_move_n.name
#         print_location(narrow_move_n.description, "treasure")
#     elif move == 'i':
#         get_and_drop(room['narrow'])
#     elif move != 'w' or 'n' or 'i':
#         print_invalid_direction()

# def move_treasure(move):
#     if move == 's':
#         treasure_move_s = room["treasure"].s_to
#         player1.current_room = treasure_move_s.name
#         print_location(treasure_move_s.description, "narrow")
#     elif move == 'i':
#         get_and_drop(room['treasure'])
#     elif move != 's' or 'i':
#         print_invalid_direction()

# def move_outside(move):
#     if move == 'n':
#         print('\nSo you choose Adventure.')
#         new_room = room['outside'].n_to
#         player1.current_room = new_room.name
#         print_location(new_room.description, "foyer")
#     elif move == 'i':
#         get_and_drop(room['outside'])
#     elif move != 'i' or 'n':
#         print('\nYou must not deny destiny, the only path forward is North. Accept faith by choosing n for North')

# print_location(room['outside'].description, "outside")
# while True:
#     try:
        
#         choices = ['n', 's', 'e', 'w', 'i']
#         next_move = input('\n~~~~> Will you explore or keep moving, traveler? ')
#         print(f"NEXT_MOVE FROM THE TOP OF THE WHILE: {next_move}")
#         print(f"PLAYER.CURRENT_ROOM: {player1.current_room}")
#         if next_move == 'q':
#             print_quit()
#             break 
#         if player1.current_room == 'Outside Cave Entrance' or player1.current_room == 'outside' and next_move in choices:
#             move_outside(next_move)
#             continue
#         if player1.current_room == 'Foyer' and next_move in choices:
#             move_foyer(next_move)
#             continue
#         if player1.current_room == 'Grand Overlook' and next_move in choices:
#             move_overlook(next_move)
#             continue
#         if player1.current_room == 'Narrow Passage' and next_move in choices:
#             move_narrow(next_move)
#             continue
#         if player1.current_room == 'Treasure Chamber' and next_move in choices:
#             move_treasure(next_move)
#             continue

#         if next_move not in choices:
#             print(f'\nPerhaps, you are more than we take you for. For now though you may only move in the four cardinal directions: n for North, s for South, e for East, w for West')
#             continue
#     except:
#         pass

from room import Room
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

# Establish routes
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Instantiate Player class
player1 = Player('Players_Gonna_Play', room['outside'].name)

def get_and_drop(room):
    print("I'M IN GET_AND_DROP")
    print(f"ROOM: {room}")
    get_items = input('Will you get or drop an item? ')
    split_items = get_items.split(' ')

    if get_items == 'no':
        return print('Carry on')

    if split_items[0] == 'get' or split_items[0] == 'take':
        item_to_get = split_items[1]
        for item in room.items:
            if item_to_get.lower() == item.name.lower():
                player1.items.append(item)
                room.on_take(item)
                split_items = []
                return print(f"You have {len(player1.items)} items, {len(room.items)} left in {player1.current_room}!!")
            
        return print('You cannot get that which the room does not contain.')

    elif split_items[0] =='drop':
        item_to_drop = split_items[1]
        for item in player1.items:
            if item_to_drop.lower() == item.name.lower():
                player1.items.remove(item)
                room.on_drop(item)
                split_items = []
                return print(f"You have {len(player1.items)} items, {len(room.items)} left in {player1.current_room}!!")
        return print('You cannot drop that which you do not have.')

def print_location(room_desc, room_name):
    print(textwrap.fill(f'\n{player1.name} is currently {player1.current_room}. {room_desc} and has {len(player1.items)} items'))
    for item in room[room_name].items:
        print(f'\nItem: {item.name.capitalize()}, Item Description: {item.description}\n')

def print_quit():
    print('\nUntil our stars align again, I bid you farewell traveler')

def print_invalid_direction():
    print('\nTherein lies that which you have not prepared for, please choose a different direction.')

def print_player_inventory():
    if len(player1.items) < 1:
        print('Inventory Empty')
    else:

        print_player_inventory()

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
    elif move == 'i':
        get_and_drop(room['foyer'])
    elif move != 's' or 'e' or 'n' or 'i':
        print_invalid_direction()

def move_overlook(move):
    if move == 's':
        overlook_move_s = room["overlook"].s_to
        player1.current_room = overlook_move_s.name
        print_location(overlook_move_s.description,"foyer" )
    elif move == 'i':
        get_and_drop(room['overlook'])
    elif move != 's' or 'i':
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
    elif move == 'i':
        get_and_drop(room['narrow'])
    elif move != 'w' or 'n' or 'i':
        print_invalid_direction()

def move_treasure(move):
    if move == 's':
        treasure_move_s = room["treasure"].s_to
        player1.current_room = treasure_move_s.name
        print_location(treasure_move_s.description, "narrow")
    elif move == 'i':
        get_and_drop(room['treasure'])
    elif move != 's' or 'i':
        print_invalid_direction()

def move_outside(move):
    if move == 'n':
        print('\nSo you choose Adventure.')
        new_room = room['outside'].n_to
        player1.current_room = new_room.name
        print_location(new_room.description, "foyer")
    elif move == 'i':
        get_and_drop(room['outside'])
    elif move != 'i' or 'n':
        print('\nYou must not deny destiny, the only path forward is North. Accept faith by choosing n for North')

print_location(room['outside'].description, "outside")
while True:
    try:
        
        choices = ['n', 's', 'e', 'w', 'i']
        next_move = input('\n~~~~> Will you explore or keep moving, traveler? ')
        print(f"NEXT_MOVE FROM THE TOP OF THE WHILE: {next_move}")
        print(f"PLAYER.CURRENT_ROOM: {player1.current_room}")
        if next_move == 'q':
            print_quit()
            break 
        if player1.current_room == 'Outside Cave Entrance' or player1.current_room == 'outside' and next_move in choices:
            move_outside(next_move)
            continue
        if player1.current_room == 'Foyer' and next_move in choices:
            move_foyer(next_move)
            continue
        if player1.current_room == 'Grand Overlook' and next_move in choices:
            move_overlook(next_move)
            continue
        if player1.current_room == 'Narrow Passage' and next_move in choices:
            move_narrow(next_move)
            continue
        if player1.current_room == 'Treasure Chamber' and next_move in choices:
            move_treasure(next_move)
            continue

        if next_move not in choices:
            print(f'\nPerhaps, you are more than we take you for. For now though you may only move in the four cardinal directions: n for North, s for South, e for East, w for West')
            continue
    except:
        pass