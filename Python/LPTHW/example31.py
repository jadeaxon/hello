#!/usr/bin/env python

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

prompt = "> "
door = raw_input(prompt)

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input(prompt)

    if bear == "1":
        print "The bear eats your face off.  Smooth move Exlax!"
    elif bear == "2":
        print "The bear eats your legs.  Have fun walking, gimp."
    else:
        print "Well, doing %s is probably better.  The bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss of Cthuhlu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input(prompt)

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Bill Cosby salutes you."
    else:
        print "The insanity rots your eyes into a pool of muck.  Hope you have a handkerchief."

else:
    print "You blither and fall on a rusty knife.  You die slowly despite your tetanus shot."


        
