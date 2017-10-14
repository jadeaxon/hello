# This module defines various parts of the game Death Ball.

from random import randint

world = [] # The game world.  An NxN grid of rooms.
size = 10 # Size in rooms of one side of the world grid.
death_balls = 3 # Number of death balls in the world.
inventory = [] # Hero's inventory.

# Populates the initial game world model.
def init_world(size, death_balls):
    for x in range(size):
        row = [] 
        for y in range(size):
            row.append([])
        world.append(row)
    world[0][0].append("hero")

    # We start with some number of death balls in random rooms.
    for i in range(death_balls):
        while True:
            x = randint(0, size - 1)
            y = randint(0, size - 1)
            # print(f"x = {x}; y = {y}") 
            # Don't start with a death ball in the starting room.
            room = world[x][y]
            # print(room)
            if "hero" in room: 
                continue
            else:
                world[x][y].append("death ball")
                break

    # Now place the treasure.
    while True:
        x = randint(0, size - 1)
        y = randint(0, size - 1)
        # print(f"x = {x}; y = {y}") 
        # Don't start with a death ball in the starting room.
        room = world[x][y]
        # print(room)
        if "hero" in room: 
            continue
        else:
            world[x][y].append("treasure")
            break

# Returns the location of the hero in the dungeon as an (x, y) tuple.
def get_hero_location():
    for x in range(size):
        for y in range(size):
            room = world[x][y]
            if "hero" in room:
                return (x, y)
    # Should throw some kind of exception.
    return (-1, -1)


# Moves the hero one room north if possible.
def go_north():
    loc = get_hero_location()
    x = loc[0]
    y = loc[1]
    y -= 1
    if (y >= 0):
        world[x][y + 1].remove("hero")
        world[x][y].append("hero")
    else:
        print("I can't go any farther north.")

# Moves the hero one room east if possible.
def go_east():
    loc = get_hero_location()
    x = loc[0]
    y = loc[1]
    x += 1
    if (x < size):
        world[x - 1][y].remove("hero")
        world[x][y].append("hero")
    else:
        print("I can't go any farther east.")

# Moves the hero one room south if possible.
def go_south():
    loc = get_hero_location()
    x = loc[0]
    y = loc[1]
    y += 1
    if (y < size):
        world[x][y - 1].remove("hero")
        world[x][y].append("hero")
    else:
        print("I can't go any farther south.")


def go_west():
    pass

# Describe room at given location.  Assumes the hero is in that room.
def describe_room(location):
    print(f"You are in room {location}.  Nothing interesting is here.")

# Updates the game world.
def update_world():
    pass


