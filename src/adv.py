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
player = Player('Dan', room['outside'])

# Write a loop that:

while True:

    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be
    # useful here).
    print("\n")
    print(player.location)
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be
# useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the
# room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

user_is_playing = True

while user_is_playing:
    print(my_player.current_room.name)
    for line in textwrap.wrap(my_player.current_room.description):
        # this returns a list of strings so we use a for loop
        print(line)

        user_input = input("which direction would you like to go? (n/e/w/s)")

        if user_input in ["n", "e", "w", "s"]:
            my_player.move(user_input)
        else:
            print("You existed the game Thanks for playing")

        user_is_playing = False
