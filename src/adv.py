from room import Room
from player import Player
from item import Item
from monster import Monster

# Declare items
item = {
    'coins': Item('coins', 'Make you richer'),
    'snack': Item('snack', 'Restore your health a little bit'),
    'potion': Item('potion', 'Restore your health a lot'),
    'dagger': Item('dagger', 'Your first weapon as a noob'),
    'sword': Item('sword', 'Better than dagger'),
    'shield': Item('shield', 'Reduce incoming damage')
}

# Declare monsters
monster = {
    'toxiccat': Monster('Toxiccat'),
    'evilhamster': Monster('Evilhamster'),
    'webmorph': Monster('Webmorph')
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

room['foyer'].items = [item['dagger']]
room['overlook'].items = [item['shield']]
room['narrow'].items = [item['snack']]
room['treasure'].items = [item['coins'], item['potion'], item['sword']]

# Add monsters to room

room['treasure'].monsters=[monster['webmorph'], monster['toxiccat']]
room['narrow'].monsters=[monster['evilhamster']]

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

print('========GAME START==========')
print(f'You are currently in: {player1.current_room.name}')
print(player1.current_room.description)
print('Commands:\nn -- move north | s -- move south | e -- move east | w -- move west |\npick [item_name] -- pick up item | drop [item_name] -- drop item |\nshow -- show available items in room | inventory -- show items in inventory |\nattack [monster name]-- attack monster  | q -- quit ')

while True:
    command = input('Enter command: ')

    if command == 'q':
        print('Goodbye')
        break
    
    elif command in ['n', 'w', 'e', 's']:
        player1.move_room(command)
        player1.current_room.show_monsters()     #as player enters new room, show monsters if there are any
    
    elif command == 'show':
        player1.current_room.show_items()
    
    elif command == 'inventory':
        player1.show_items()
    
    elif len(command.split()) == 2:
        if command.split()[0] == 'take':
            player1.take(command.split()[1])
        elif command.split()[0] == 'drop':
            player1.drop(command.split()[1])
        elif command.split()[0] == 'attack':
            player1.attack(command.split()[1])
            player1.current_room.show_monsters()       #show remaining monsters in the room if there are any
    
    else:
        print('Please enter a valid command (n, s, e, w, pick [item], drop [item], show, inventory q).')
        continue
