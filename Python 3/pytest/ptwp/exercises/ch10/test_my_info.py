from unittest import mock
import my_info
from pathlib import Path

def test_my_home_returns_correct_value():
    with mock.patch('pathlib.Path.home') as mock_home:
        mock_home.return_value = Path("/users/fake_user")
        value = my_info.home_dir()
        assert value == "/users/fake_user"

def test_my_home_is_called():
    with mock.patch('pathlib.Path.home') as mock_home:
        my_info.home_dir()
        mock_home.assert_called_with()
