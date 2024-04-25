# Unit tests using pytest.

def formatted_name(first, last):
    result = f'{first.title()} {last.title()}'
    return result

name = formatted_name('jeff', 'anderson')
print(name)

# A test case is a collection of unit tests.
# pytest tests must start with test_.
# Run these tests in shell using 'pytest unit_tests.py'.
# Normally, you'd put these tests in test_*.py files. Then pytest would find the files automatically too.
def test_both_lowercase():
    name = formatted_name('bob', 'marley')
    assert name == 'Bob Marley'

def test_both_uppercase():
    name = formatted_name('LUKE', 'SKYWALKER')
    assert name == 'Luke Skywalker'

def test_that_fails():
    name = formatted_name('Davy', 'Crockett')
    assert name == 'David Crockpot'
    # Raises an AssertionError

# To test classes, just create class instances in the tests.
from dog import Warg

def test_warg_rage():
    warg = Warg('Jaws', 4)
    warg.attack()
    assert warg.rage == 1

import pytest

# You can create a test fixture by using a function decorator.
# Aspect-oriented programming.
# Looks like the name of the fixture function has to match the name of the arg passed to test functions. Yup.
@pytest.fixture
def warg():
    warg = Warg('Testy', 5)
    return warg

# The fixture gets passed in as the arg.
def test_warg_rage2(warg):
    warg.attack()
    assert warg.rage == 1












