from room import Room
from player import Player
import textwrap
from item import Item

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

# Create Items
items = {
    'headlight': Item('headlight', 'wear it to light up dark rooms'),
    'sword': Item('sword', 'Used it to fight of the guards of the treasure'),
    'binoculars': Item('binoculars', 'Used to see out on overlook')
}

# Add items to room
room['outside'].items.append(items['headlight'])
room['overlook'].items.append(items['binoculars'])
room['treasure'].items.append(items['sword'])

#
# Main
#
# tries to move the player in a specific direction


def try_direction(player, direction):
    # this will check the player current location, and when the player
    # enter a first_char to make a move it would check to see if there is
    # a room in that specific direction. they are moved to that room else
    #  if there are no room print a message saying "You cannot go there"
    # and the player is not moved.
    attribute = direction + '_to'

    # Python 'hasattr' allows us to check if a class has an attribute
    if hasattr(player.location, attribute):
        # this checks if the entry was a valid direction.
        # 'getattr' fetches the value associated with the attribute
        player.location = getattr(player.location, attribute)  # fetch
        # the player old location with the attribute and update it to the new
        # location base on the entry the player entered.


# Make a new player object that is currently in the 'outside' room.
player = Player("Dan", room['outside'])

# Write a loop that:

while True:

    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be
    # useful here).
    # print("\n")
    print("Player:", player.name)
    print("Current Location:", player.location)
    # prints currently held items
    print(f'\nHeld Items: {player.location.list_items()}\n')

    # for line in textwrap.wrap(player.location):
    #     print(line)

# * Waits for user input and decides what to do.
    # will return a list not str
    first_char = input(
        "\nchoose your direction e/w/n/s/ or q to quit game:").strip().lower().split()
    first_first_char = first_char[0]
    first_char = first_first_char[0]
# If the user enters "q", quit the game.
    if first_char == 'q':
        print(player.name)
        print("You have exited the game, Thanks for playing.")
        break

    #
    # If the user enters a cardinal direction, attempt to move to the
    # room there.
    # Print an error message if the movement isn't allowed.
    # user can enter 'east', 'west', 'north', 'south' or
    # let the them enter 'e' , 'w' 'n' 's' in order to move.
    # so to do this I will strip everything the first character.

    if first_char == 'n':
        # move to the north
        try_direction(player, first_char)
    elif first_char == 's':
        # move to the south
        try_direction(player, first_char)
    elif first_char == 'e':
        # move to the east
        try_direction(player, first_char)
    elif first_char == 'w':
        # move to the west
        try_direction(player, first_char)

        #
