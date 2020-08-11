"""
Basic Hello World program in AdventureLib

This program is designed to demonstrate the basic capabilities
of AdventureLib. It will:
- Create a simple three room world
- Add a single inventory item
- Require that inventory item to move to the final room
"""

# Import the library contents
from adventurelib import *

# Define our rooms
bedroom = Room(
    """
You are in your bedroom. The bed is unmade, but otherwise
it's clean. Your dresser is in the corner, and a desk is
under the window.
"""
)

living_room = Room(
    """
The living room stands bright and empty. The TV is off,
and the sun shines brightly through the curtains.
"""
)

front_porch = Room(
    """
The creaky boards of your front porch welcome you as an
old friend. Your front door mat reads 'Welcome'.
"""
)

# Define the connections between the rooms
bedroom.south = living_room
living_room.east = front_porch

# Define a constraint to move from the bedroom to the livingroom
# If the door between the living room and front porch door is locked,
# we can't exit
living_room.locked = {"east": True}

# None of the other rooms have any locked doors
bedroom.locked = dict()
front_porch.locked = dict()

# Set the starting room as the current room
current_room = bedroom


# Define functions to use items
def unlock_living_room(current_room):

    if current_room == living_room:
        print("You unlock the door.")
        current_room.locked["east"] = False
    else:
        print("There is nothing to unlock here.")


# Create our items
key = Item("a front door key", "key")
key.use_item = unlock_living_room

# Create empty Bags for room contents
bedroom.contents = Bag()
living_room.contents = Bag()
front_porch.contents = Bag()

# Put the key in the bedroom
bedroom.contents.add(key)

# Setup our current empty inventory
inventory = Bag()


# Define our movement commands
@when("go DIRECTION")
@when("north", direction="north")
@when("south", direction="south")
@when("east", direction="east")
@when("west", direction="west")
@when("n", direction="north")
@when("s", direction="south")
@when("e", direction="east")
@when("w", direction="west")
def go(direction: str):
    """Processes our moving direction

    Arguments:
        direction {str} -- which direction does the player want to move
    """

    # What is our current room
    global current_room

    # Is there an exit in that direction
    next_room = current_room.exit(direction)
    if next_room:
        # Is the door locked?
        if direction in current_room.locked and current_room.locked[direction]:
            print(f"You can't go {direction} --- the door is locked.")
        else:
            current_room = next_room
            print(f"You go {direction}.")
            look()

    # No exit that way
    else:
        print(f"You can't go {direction}.")


# How do we look at the room
@when("look")
def look():
    """Looks at the current room"""
    global current_room

    # Describe the room
    say(f"{current_room}")

    # List the contents
    for item in current_room.contents:
        print(f"There is {item} here.")

    # List the exits
    print(f"The following exits are present: {current_room.exits()}")


# How do we look at items?
@when("look at ITEM")
@when("inspect ITEM")
def look_at(item: str):

    # Check if the item is in our inventory or not
    obj = inventory.find(item)
    if not obj:
        print(f"You don't have {item}.")
    else:
        print(f"It's an {obj}.")


# How do we pick up items?
@when("take ITEM")
@when("get ITEM")
@when("pickup ITEM")
def get(item: str):
    """Get the item if it exists

    Arguments:
        item {str} -- The name of the item to get
    """
    global current_room

    obj = current_room.contents.take(item)
    if not obj:
        print(f"There is no {item} here.")
    else:
        print(f"You now have {item}.")
        inventory.add(obj)


# How do we use an item?
@when("unlock door", item="key")
@when("use ITEM")
def use(item: str):
    """Use an item, consumes it if used

    Arguments:
        item {str} -- Which item to use
    """

    global inventory

    # First, do we have the item?
    obj = inventory.take(item)
    if not obj:
        print(f"You don't have {item}")

    # Try to use the item
    else:
        obj.use_item(current_room)


if __name__ == "__main__":
    start()
