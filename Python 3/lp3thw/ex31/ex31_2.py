#!/usr/bin/env python3

# This game is called 2x2.  You are in a small 2x2 grid.  You can move north, south, east, or west.
# It's basically a hard-coded state machine with four transitions in each room.

room = "(0, 0)" # What room you are in.
prompt = "{}> " # Prompt for next action.
teleports = 0 # How many times you have been teleported.

print("Welcome to 2x2!")
print("Your quest is to escape this dungeon without dying.")
while True:
    action = input(prompt.format(room))
    if action == "q": 
        print("Thanks for playing 2x2!")
        break # Quit the game. 
    if room == "(0, 0)":
        if action == "n":
            room = "(0, 0)"
        elif action == "e":
            room = "(0, 1)"
        elif action == "w":
            room = "(0, 0)"
        elif action == "s":
            room = "(1, 0)"
        else:
            print(f"I don't know how to '{action}'.")
    elif room == "(0, 1)":
        if action == "n":
            room = "(0, 1)"
        elif action == "e":
            print("You get hit by a 2x4 and die.")
            break # Game over.
        elif action == "w":
            room = "(0, 0)"
        elif action == "s":
            room = "(1, 1)"
        else:
            print(f"I don't know how to '{action}'.")
    elif room == "(1, 0)":
        if action == "n":
            room = "(0, 0)"
        elif action == "e":
            room = "(1, 1)"
        elif action == "w":
            print("You found the exit.  You win!")
            break # Victory
        elif action == "s":
            room = "(1, 0)"
        else:
            print(f"I don't know how to '{action}'.")
    elif room == "(1, 1)":
        if action == "n":
            room = "(0, 1)"
        elif action == "e":
            room = "(1, 1)"
        elif action == "w":
            room = "(1, 0)"
        elif action == "s":
            room = "(2, 2)" # Secret passage.
        else:
            print(f"I don't know how to '{action}'.")
    else:
        print(f"How the heck did you get into room {room}?")
        if teleports < 2:
            print("You have been teleported to room (0, 0).")
            teleports += 1
        else:
            print("You die in a teleporter accident.")
            break # You lose.
        room = "(0, 0)"


