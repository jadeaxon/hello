#!/usr/bin/env python3

# A text adventure game.  Each function represents a character state
# (usually physical location in a room).

from sys import exit

inventory = []

# Handles character interaction with the gold room.
def gold_room():
    print("This room is full of gold.  How much do you take?")

    while True:
        try:
            choice = input("> ")
            how_much = int(choice)
            break # We have a valid number.
        except ValueError:
            print(f"'{choice}' is not a positive number.  Try again.")
        

    if how_much <= 0:
        if "honey" not in inventory:
            dead("You took too little gold to pay for lunch on the way home.  You starve to death.")
        else:
            print("YOU WIN!")
            print("Luckily you had some honey since you didn't take enough gold to pay for lunch.")
            exit(0)
    if how_much < 50:
        print("YOU WIN!")
        print("Nice, you're not greedy.")
        exit(0)
    else:
        dead("You greedy bastard!")

# Handles character interaction with the bear room and its deadly denizen.
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    bear_dead = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            if not bear_dead:
                dead("The bear looks at you then slaps your face off.")
            else:
                print("You take the honey.")
                inventory.append("honey")
        elif choice == "taunt bear" and not bear_moved:
            if not bear_dead:
                print("The bear has moved from the door.")
                print("You can go through it now.")
                bear_moved = True
            else:
                print("Really?  You are going to taunt a dead bear?  What a jerk.")
        elif choice == "taunt bear" and bear_moved:
            if not bear_dead:
                dead("The bear gets pissed and chews your leg off.")
            else:
                print("Really?  You are going to taunt a dead bear?  What a jerk.")

        elif choice == "open door" and (bear_moved or bear_dead):
            gold_room()
        elif choice == "attack bear":
            if "axe" in inventory:
                print("You chop the bear in half with your trusty axe.")
                bear_dead = True
            else:
                dead("You foolishly attacked a bear with your bare hands.  WDYTWGTH?!")

        else:
            print(f"I don't know how to '{choice}'.")

# Handles character interaction with the basement.
def basement():
    if not "axe" in inventory:
        print("There is an axe here.")
    else:
        print("There is nothing here.")

    choice = input("> ")
    if choice == "take axe":
        print("You take the axe.")
        inventory.append("axe")
        basement()
    elif choice == "up":
        start()
    else:
        print(f"You aimlessly {choice} for a while.  Nothing happens.")
        basement()


# Handles character interaction with the Cthulhu room and the evil therein.
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice or "eat" in choice:
        dead("Well, that was tasty!  However, it was required for survival.")
    else:
        cthulhu_room()

# Represents the usual end state of the character.
def dead(reason):
    print("YOU ARE DEAD!") 
    print(reason, " Nice work!")
    exit(0)

# Handles character interaction with the starting room.
def start():
    print("You are in a dark room.")
    print("There are two doors: one to your right and one to your left.")
    print("There is also a trap door leading to a basement.") 
    print("Which one do you go through?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice in ["trap", "basement", "trapdoor", "trap door"]:
        basement()
    else:
        dead("You stumble around the room until you starve to death.")


# Start the adventure that will almost certainly lead to your death.
start()
