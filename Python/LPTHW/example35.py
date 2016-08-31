#!/usr/bin/env python

from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    prompt = "> "
    answer = raw_input(prompt)
    if "0" in answer or "1" in answer:
        how_much = int(answer)
    else:
        dead("Man, learn to type a number!")


    if how_much < 50:
        print "You have chosen . . . wisely.  Go in peace."
        exit(0)
    else:
        dead("Die, you greedy bastard!")



def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is blocking the other door in this room."
    print "How are you going to get past the bear?"

    prompt = "> "
    bear_moved = False

    while True:
        action = raw_input(prompt)

        if action == "take honey":
            dead("The bear growls and slaps your face off.  You kind of needed that to live.")
        elif action == "taunt bear" and not bear_moved:
            print "The bear moves away from the door."
            bear_moved = True
        elif action == "taunt bear" and bear_moved:
            dead("The bear uses you as a snack.")
        elif action == "open door" and bear_moved:
            gold_room()
        else:
            print "You do not know how to %r." % action

def cthulu_room():
    print "Here you see the evil Cthulu."
    print "It stares at you and you go insane."
    print "Do you flee your life or eat your head?"

    prompt = "> "
    action = raw_input(prompt)

    if "flee" in action:
        start()
    elif "head" in action:
        dead("Your last thought is how tasty your head was.")
    else:
        cthulu_room()

def dead(reason):
    print "You are dead, dumb ass.", reason
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and a door to your left."
    print "Which door do you take?"

    prompt = "> "
    action = raw_input(prompt)

    if action == "left":
        bear_room()
    elif action == "right":
        cthulu_room()
    else:
        dead("You starve to death due to indecision.")


start()



