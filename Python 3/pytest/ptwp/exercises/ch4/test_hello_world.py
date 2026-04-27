import pytest
from hello_world import hello
import os

@pytest.fixture()
def hello_output(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path) # Temporarily change directory to temporary directory.
    print(os.getcwd())
    hello()
    with open('hello.txt', "r") as f:
        r = f.read()
        yield r

def test_hello_world(hello_output):
    assert hello_output == 'Hello, world!\n'


