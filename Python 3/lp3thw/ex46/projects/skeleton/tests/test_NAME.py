from nose.tools import *
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test__basic():
    print("I RAN!")

def test_two():
    print("Another test.")

