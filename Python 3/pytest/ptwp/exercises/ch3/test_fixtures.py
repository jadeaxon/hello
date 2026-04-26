import pytest

@pytest.fixture()
def a_tuple():
    """Create a tuple."""
    return (1, 2, 3)

@pytest.fixture(scope="module")
def a_list():
    """Create a module-scope list."""
    print("Setting up a_list fixture.")
    yield [4, 5, 6]
    print("Tearing down a_list fixture.")

@pytest.fixture()
def a_dict():
    """Create a dictionary."""
    return {"one": 1, "two": 2, "three": 3}


def test_tuple(a_tuple):
    r = a_tuple + (4, 5, 6)
    assert len(r) == 6

def test_list_append(a_list):
    a_list.append(7)
    assert len(a_list) == 4

def test_list_pop(a_list):
    r = a_list.pop()
    assert r == 7
    assert len(a_list) == 3

def test_dict(a_dict):
    a_dict.popitem()
    assert "two" in a_dict # should have popped last inserted

