"""
Test Cases
* `list` from an empty database
* `list` from a non-empty database
"""
from cards import Card
from cards import MissingSummary
import pytest

def test_list_no_cards(cards_db):
    """Empty db, empty list"""
    assert cards_db.list_cards() == []


def test_list_several_cards(cards_db):
    """
    Given a variety of cards, make sure they get returned.
    """
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards()

    assert len(the_list) == len(orig)
    for c in orig:
        assert c in the_list


def test_list_card_without_summary(cards_db):
    card = Card("", owner="me", state="todo")
    with pytest.raises(MissingSummary) as e_info:
        cards_db.add_card(card)


def test_list_filter_by_owner(cards_db):
    card = Card("test", owner="me", state="todo")
    card2 = Card("test", owner="thee", state="todo")
    cards_db.add_card(card)
    cards_db.add_card(card2)
    cards = cards_db.list_cards(owner="me")
    assert cards[0] == card


def test_list_filter_by_state(cards_db):
    card = Card("test", owner="me", state="todo")
    card2 = Card("test", owner="me", state="done")
    cards_db.add_card(card)
    cards_db.add_card(card2)
    cards = cards_db.list_cards(state="todo")
    assert cards[0] == card


def test_list_filter_by_owner_and_state(cards_db):
    card = Card("test", owner="me", state="todo")
    card2 = Card("test", owner="thee", state="done")
    cards_db.add_card(card)
    cards_db.add_card(card2)
    cards = cards_db.list_cards(owner="me", state="todo")
    assert cards[0] == card

