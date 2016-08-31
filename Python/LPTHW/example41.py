#!/usr/bin/env python

from sys import exit
from random import randint


prompt = "> "

def death():
    quips = [
        "You died.  You kind of suck at this.",
        "Nice job.  You died, jackass.",
        "Luser.",
        "My dead puppy is better at this than you are."
    ]

    print quips[randint(0, len(quips) - 1)]
    exit(1)

def central_corridor():
    global prompt

    print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
    print "your entire crew.  You are the last surviving member.  Your last mission"
    print "is to get the neutron destruct bomb from the Armory, plant it on the"
    
    print "bridge, and hopefully escape in an escape pod before the ship blows."
    print "\n"
    print "You're running down the central corridor to the Armory.  A Gothon jumps"
    print "out.  Red scaly skin and dark grimy teeth compliment the evil clown"
    print "costume which flows menacingly around his hate-filled body.  He blocks"
    print "the door to the Armory and reaches for his blaster."

    action = raw_input(prompt)

    if action == "shoot":
        print "You blast him.  Only to hit his costume.  He gets mad and eats you."
        return 'death'

    elif action == "dodge":
        print "You fall and hit your head on the ground.  The Gothon eats you."
        return 'death'

    elif action == "tell a joke":
        print "He laughs so hard you have no trouble walking up to him and"
        print "blasting a hole through his head.  You enter the Armory."
        return 'armory'

    else: # Player does something unexpected.
        print  "Bogus operator detected."
        return 'central_corridor'


def armory():
    global prompt
    print "You are in the armory.  The lockbox with the bomb in it has a key"
    print "coded lock with three digits.  You have ten tries to guess the code."
    print "What code do you enter?"

    code = "%d%d%d" % ( randint(1, 9),  randint(1, 9),  randint(1, 9) )
    guess = raw_input(prompt)
    tries = 0

    while (guess != code) and (tries < 10):
        if guess == "777":
            code = "777"
            break

        print "BZZZZZZZZZZZZZT!"
        tries += 1
        guess = raw_input(prompt)

    if guess == code:
        print "Click!  You get the bomb and head for the bridge."
        return 'the_bridge'
    else:
        print "The lock fuses.  You wait in despair.  A Gothon scout"
        print "eventually finds you and puts you out of your misery."
        return 'death'


def the_bridge():
    global prompt
    print "You burst onto the bridge.  You are greeted by five Gothons,"
    print "each uglier than the next.  The bomb you are carring alarms"
    print "them."

    action = raw_input(prompt)

    if action == "throw the bomb":
        print "In panic, you throw the bomb.  As you turn to run, you"
        print "are shot in the back by the ugliest of the Gothons."
        print "You die knowing at least they'll be dead soon too."
        return 'death'

    elif action == "slowly place the bomb":
        print "You slowly place the bomb, keeping your blaster pointed at it."
        print "The Gothons are afraid to make a move.  You back out of the"
        print "room and make a mad dash for the escape pod."
        return 'escape_pod'

    else:
        print "Bogus operator detected.  Try something else."
        return 'the_bridge'

def escape_pod():
    global prompt
    print "There are five escape pods here.  Which one do you take?"
    safe_pod = randint(1, 5)

    choice = raw_input(prompt)

    if int(choice) != safe_pod:
        print "You enter the pod.  It launches into space.  \"Safe"
        print "at last\" you think.  Then, the damaged pod implodes"
        print "and turns you into a blendo."
        return 'death'
    else: # You picked the safe pod.
        print "You enter the pod.  It launches into space.  You watch"
        print "with satifaction as your ship blows up, turning the Gothons"
        print "into dust.  Your crew was incompetent and your ship was"
        print "getting old anyway.  Hopefully you'll get a promotion,"
        print "a new ship, and a better crew out of this deal."
        exit(0)


rooms = {
    'death': death,
    'central_corridor': central_corridor,
    'armory': armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod

} # rooms

def runner(map, start):
    next = start;

    while True:
        room = map[next]
        print "\n------------------------------"
        # We are calling the function named by the value of room.
        # We are not calling the function 'room'.
        # What if we had defined a function named room?
        next = room()


runner(rooms, 'central_corridor')




