import pytest
from ex49.game import Room
import ex49.parser as parser

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


#==============================================================================
# Parser Module
#==============================================================================

def test__peek():
    words = [("direction", "north"), ("noun", "bear")]
    words2 = [("direction", "north"), ("noun", "bear")]
    word = parser.peek(words)
    assert_equal(("direction", "north"), word)
    assert_equal(words, words2)

def test__tokenize__directions():
    assert_equal(parser.tokenize("north"), [("direction", "north")])
    result = parser.tokenize("north south east")
    assert_equal(
        result,
        [("direction", "north"), ("direction", "south"), ("direction", "east")]
    )

def test__tokenize__verbs():
    assert_equal(parser.tokenize("go"), [("verb", "go")])
    result = parser.tokenize("go kill eat")
    assert_equal(
        result,
        [("verb", "go"), ("verb", "kill"), ("verb", "eat")]
    )

def test__tokenize__nouns():
    assert_equal(parser.tokenize("bear"), [("noun", "bear")])
    result = parser.tokenize("bear princess")
    assert_equal(
        result,
        [("noun", "bear"), ("noun", "princess")]
    )

def test__tokenize__numbers():
    assert_equal(parser.tokenize("1234"), [("number", 1234)])
    result = parser.tokenize("567 789")
    assert_equal(
        result,
        [("number", 567), ("number", 789)]
    )

def test__tokenize__prepositions():
    assert_equal(parser.tokenize("to"), [("preposition", "to")])
    result = parser.tokenize("from into")
    assert_equal(
        result,
        [("preposition", "from"), ("preposition", "into")]
    )

def test__tokenize__articles():
    assert_equal(parser.tokenize("a"), [("article", "a")])
    result = parser.tokenize("an the")
    assert_equal(
        result,
        [("article", "an"), ("article", "the")]
    )

def test__tokenize__errors():
    assert_equal(parser.tokenize("ABCDEFG"), [("error", "ABCDEFG")])
    result = parser.tokenize("HIJKLMNO C3P0")
    assert_equal(
        result,
        [("error", "HIJKLMNO"), ("error", "C3P0")]
    )


#==============================================================================
# Room Class
#==============================================================================

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





