import pytest
from ex47.game import Room

# What is the equivalent in pytest?  These both seem to work in pytest.
def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test__basic():
    print("I RAN!")

# This existed in nose but maybe not in pytest.
def assert_equal(a, b):
    assert a == b

def test__Room():
    room = Room("Gold Room", "There is gold in this room.")
    assert_equal(room.name, "Gold Room")
    assert_equal(room.paths, {})

def test__Room__paths():
    center = Room("Center", "Stuck in the middle with you.")
    north = Room("North", "It's cold in Canada.");
    south = Room("South", "You see James Taylor here.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test__Room__map():
    start = Room("Start", "You are at the beginning.")
    west = Room("Trees", "There are trees here.")
    down = Room("Dungeon", "It's dark here.  A grue is going to eat you!")
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
    # assert_equal(3, 2)



