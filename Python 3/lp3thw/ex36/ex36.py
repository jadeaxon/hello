#!/usr/bin/env python3

from deathball import *

# You're in a 10x10 grid.  Room (0,0).
# There are n death balls that move randomly.
# If you enter a room with a death ball you die.
# You see a strong glow adjacent.  Faint 2 rooms away.
# Yellow glow for treasure.

#==============================================================================
# Main
#==============================================================================

init_world(10, 3)
# print(world)

print("Welcome to Death Ball!")
print("Try to find the treasure and escape without being killed by one of the death balls.")

while True:
    location = get_hero_location()
    describe_room(location)
    action = input(f"{location}> ")
    if action in "nN":
        go_north()
    elif action in "eE":
        go_east()
    elif action in "sS":
        go_south()
    elif action in "wW":
        go_west()
    elif action == "cheat":
        print(world)
    elif action == "exit" or action == "quit":
        break
    else:
        print(f"I don't know how to '{action}'.")
    update_world()




