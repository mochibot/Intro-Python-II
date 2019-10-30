from room import Room
from player import Player
from item import Item

# Declar items
item = {
    'coins': Item('coins', 'Make you richer'),
    'snack': Item('snack', 'Restore your health a little bit'),
    'potion': Item('potion', 'Restore your health a lot'),
    'dagger': Item('dagger', 'Your first weapon as a noob'),
    'sword': Item('sword', 'Better than dagger'),
    'shield': Item('shield', 'Reduce incoming damage')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", 
                     """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", 
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", 
                     """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", 
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

# Add items to room

room['foyer'].items = [item['snack']]
room['overlook'].items = [item['shield']]
room['narrow'].items = [item['dagger']]
room['treasure'].items = [item['coins'], item['potion'], item['sword']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Player1', room['outside'])

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

'''
while True:
    print(f'You are currently in: {player1.current_room.name}')
    print(player1.current_room.description)
    print('Commands: n -- move north | s -- move south | e -- move east | w -- move west | q -- quit')
    input_direction = input('Enter the direction to move to: ')

    if input_direction == 'q':
        print('Goodbye')
        break
    elif input_direction == 'n' or input_direction == 'w' or input_direction =='e' or input_direction == 's':
        player1.move_room(input_direction)
    else:
        print('Please select a valid option (n, s, e, w, q).')
        continue
'''