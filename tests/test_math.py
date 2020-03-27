import pytest
from gameApp.math import bp


def test_home(client):
    response = client.get('/')
    assert b'Simple Math Game App' in response.data
    assert b'click the button to start and Good Luck!' in response.data
    assert b'start' in response.data
