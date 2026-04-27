import pytest
from cards import Card

def test_start_from_in_prog(cards_db):
    index = cards_db.add_card(Card("second edition", state="in prog"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_from_done(cards_db):
    index = cards_db.add_card(Card("write a book", state="done"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_from_todo(cards_db):
    index = cards_db.add_card(Card("create a course", state="todo"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

# Do the same as above using 3 different forms of parameterization.
@pytest.mark.parametrize("start_state", ["in prog", "done", "todo"])
def test_start(cards_db, start_state):
    index = cards_db.add_card(Card("do something", state=start_state))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

@pytest.fixture(params=["in prog", "done", "todo"])
def start_state_p(request):
    return request.param

def test_start_p(cards_db, start_state_p):
    index = cards_db.add_card(Card("do something", state=start_state_p))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

def pytest_generate_tests(metafunc):
    if "start_state_pgt" in metafunc.fixturenames:
        metafunc.parametrize("start_state_pgt", ["in prog", "done", "todo"])

def test_start_pgt(cards_db, start_state_pgt):
    index = cards_db.add_card(Card("do something", state=start_state_pgt))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

