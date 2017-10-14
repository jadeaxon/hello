#!/usr/bin/env python3

print("""You enter a dark room with two doors.
Do you go through door #1, #2, or #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. The cake is a lie.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    elif bear == "3":
        print("The bear starves to death.  You pass safely.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    print("4. Yo mama.")

    insanity = input("> ")

    if (insanity == "1") or (insanity == "2"):
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    elif (insanity == "4"):
        print("Your witty comeback causes Cthulhu to blink allowing your to regain your previous level of sanity.")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif door == "3":
    print("A bottomless pit lies before you.")
    print("1. Step around it.")
    print("2. Step onto it.")
    pit = input("> ")
    if pit == "1":
        print("You fall to your doom.  I told you it lies!")
    elif pit == "2":
        print("That pit lies.  You make it safely past it.")
    else:
        print("Doing '{pit}' triggers a cave in.  You are dead!")
else:
    print("You stumble around and fall on a knife and die.  Good job!")


