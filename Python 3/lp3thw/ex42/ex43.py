#!/usr/bin/env python3

from sys import exit
from random import randint
from textwrap import dedent

# A scene in the game.  Roughly equivalent to a room but more flexible.
class Scene(object):
    def enter(self):
        print("Abstract base class. Subclass Scene to use.")
        exit(1)

# The game engine.
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # The game starts with an opening scene.
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        # Our action in a scene will cause a transition to a (new) scene.
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # Be sure to print out the last scene.
        current_scene.enter()

# A scene in which you die.
class Death(Scene):
    quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if you didn't suck at this so much.",
        "Luser.",
        "I have a small puppy that's better at this.",
        "Bogus operator detected.",
    ]

    def enter(self):
        i = randint(0, len(Death.quips) - 1)
        quip = Death.quips[i]
        print(quip)
        print("YOU LOSE!") 
        exit(1)

# A scene on the spaceship.
class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal have invaded your ship and destroyed your entire crew.
            You are the last surviving member.  Your final mission is to get the netron destruct
            bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting
            to an escape pod.
            You're running down the central corridor to the Weapons Armory when a Gothon jumps
            out--red, scaly skin, dark grimy teeth, and evil clown costume flowing around his
            hate-filled body.  He's blocking the door to the Armory and about to vaporize you with
            his blaster weapon.
        """))
        action = input("> ")
        if action in ["shoot", "attack", "kill"]:
            counterattack = randint(1, 3) # Combat system.
            if counterattack == 3:
                print(dedent("""Quick on the draw, you yank out your blaster and fire it at the Gothon.
                His clown costume is flowing and moving around his body, which throws off your aim.
                Your laser hits his costume but misses him completely.  This entirely ruins his brand
                new costume that his mother bought him, which makes him fly into an insane rage and
                blast you repeately in the face until you disintegrate.  He then eats your ashes.
                """))
                return 'death'
            else:
                print(dedent("""
                    You're quick on the draw but bad on the aim.  Luckily the Gothon can't hit the
                    broad side of a transport either.  You are both still alive--for now.
                """))
                return 'central_corridor'
        elif action in ["dodge", "run", "evade"]:
            attack = randint(1, 3) # Combat system.
            if attack == 3:
                print(dedent("""
                    Like a world-class boxer, you dodge, weave, slip, and slide right as the Gothon's
                    blaster cranks a laser past your head.  In the middle of your artful dodge, your
                    foot slips and you bang your head on the metal wall and pass out.  You wake up
                    shortly after only to die as the Gothon stomps on your head and eats you.
                """))
                return 'death'
            else:
                print(dedent("""
                    Your amusing movements only seem to have angered the Gothon.  He tries to kill
                    you but missed this time.
                """))
                return 'central_corridor'
        elif action in ['tell a joke', 'tell joke', 'joke']:
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the academy.  You tell the one
                Gothon joke you know: Lbhe zbgure vf fb snng, jura fur fvgf nebhaq gur ubhfr, fur
                fvgf nebhaq gur ubhfr.  The Gothon stops, tries not to laung, then busts out
                laughing and can't move.  While he's laughing, you run up and shoot him square in
                the head, putting him down.  You jump through the Weapon Armory door.
            """))
            return 'laser_weapon_armory'
        else:
            print(f"ERROR!  I do not know how to '{action}'.")
            return 'central corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons
            that might be hiding.  It's dead quiet, too quiet.  You stand up and run to the far side
            of the room and find the neutron momb in its container.  There's a keypad lock on the
            box and you need the code to get the bomb out.  If you get the code wrong 10 times then
            the lock lcoses forever and you can't get the bomb.  The code is 3 digits.
        """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guesses = 0
        guess = "000" 
        while (guess != code) and (guesses < 10):
            print("BZZZZEDDD!")
            guesses += 1
            guess = input(f"[keypad]{guesses}> ")
            guess = guess.strip()

            if guess == code:
                print(dedent("""
                    The container clicks open and the seal breaks, letting gas out.  You grab the
                    neutron bomb and run as fast as you can to the bridge where you must place it in
                    the right spot.
                """))
                return 'the_bridge'
            elif guess == "007":
                print(f"The code is {code}.") # James Bond skills.
            elif guess == "joke":
                print(dedent("""
                    You are on a roll.  Your joke about there being only 10 kinds of people causes
                    the AI in the pad control to malfunction and release the lock.  You grab the
                    bomb and head for the bridge.
                """))
                return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a sickening melting sound as the
                mechanism is fused together.  You decide to sit there, and finally the Gothons
                blow up the ship from their ship and you die horribly.
            """))
            print(f"The code was {code}.")
            return "death"

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5
            Gothons who are trying to take control of the ship.  Each of them has an even glier
            clown costume than the last.  They have't pulled their weapons out yet, as the see the
            active bomb under your arm and don't want to set it off.
        """))
        action = input("> ")
        if action in ["throw the bomb", "throw bomb"]:
            luck = randint(1, 3)
            if luck == 3:
                print(dedent("""
                    In a panic you throw the bomb at the group of Gothons and make a leap for the door.
                    Righth as you drop it a Gothon shouuts you right in the back, killing you.  As you
                    die you see another Gothon frantically try to disarm the bomb.  You die knowing at
                    least they will all get blown up soon.
                """))
                return 'death'
            else:
                print(dedent("""
                    Despite your foolishness, luck saves the day.  The bomb bounces back into your
                    hands giving you another chance to do something less likely to result in your
                    death.
                """))
                return 'the_bridge'
        elif action in ["slowly place the bomb", "place bomb"]:
            print(dedent("""
                You point your blaster at the bomb under your arm and the Gothons put their hands up and
            start to sweat.  You inch backward to the door, open it, and then carefully place the
            bomb on the floor, pointing your blaster at it.  You then jump back through the door,
            punch the close button and blast the lock so the Gothns can't get out.  Now that the
            bomb is placed, you run to the escape pod to get off this tin can.
            """))
            return 'escape_pod'
        elif "joke" in action:
            print(dedent("""
                You should have been a comedian, not a doctor.  Your witty barb incapacitates the Gothon marauders
                allowing you to easily place the bomb and make your way to the escape pods.
            """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
            You rush through the ship, desparetly trying to make it to the escape pod before the
            whole ship explodes.  It seems like hardly any Gothons are on the ship, so your run is
            clear of interferenc.  You get to the chamber with the escape pods, and now need to pick
            one to tak.  Some of them could be damaged but you don't have time to look.  There're 5
            pods.  Which one do you take?
        """))
        good_pod = randint(1, 5)
        guess = 0 
        while True:
            guess = input("[pod #]> ")
            if guess == "diagnostic":
                print(f"The good pod is pod {good_pod}.")
            else:
                break
        if guess == "joke":
            print(dedent(f"""
                You're right, it is a joke to determine which escape pod is still functional.  You
                easly select pop {good_pod}.
            """))
            print("YOU WIN!")
            return 'finished'
        elif int(guess) != good_pod:
            print(dedent(f"""
                You jump int pod {guess} and hit the eject button.  The pod escapes out into the
                void of space and then implodes as the hull ruptures, crushing your body into jam
                jelly.
            """))
            return 'death'
        else:
            print(dedent(f"""
                You jump into pod {guess} and hit the eject button.  The pod easily slides out into
                space heading to the planet below.  As it flies to the planet, you look back and see
                your ship implode then explode like a bright star, taking out the Gothon ship at the
                same time.
            """))
            print("YOU WIN!")
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won!  Good job!")
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

