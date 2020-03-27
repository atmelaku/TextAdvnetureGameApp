import pytest
from gameApp.math import bp


def test_home(client):
    response = client.get('/')
    assert b'Simple Math Game App' in response.data
    assert b'click the button to start and Good Luck!' in response.data
    assert b'start' in response.data

def test_one(client):

    response = client.get('/1')
    assert response.status_code == 200
    assert b'wellcome to part one simple math game' in response.data
    assert b'1. what is the sum of one and two?' in response.data
    assert b'2. what is the sum of six and two?' in response.data
    assert b'3. what is the sum of two and two?' in response.data
    assert b'4. what is the sum of five and two?' in response.data
    assert b'answer' in response.data
    assert b'<input type="submit"' in response.data
    assert b'homepage' in response.data
    assert b'level1' in response.data
    assert b'level2' in response.data
    assert b'level3' in response.data
    assert b'level4' in response.data
    response = client.post('/1', data={'answer1': '3', 'answer2': '8', 'answer3': '4', 'answer4': '7'})
    assert b'100%, nice Job!, try the next level' not in response.data
    response = client.post('/1', data={'answer1': '3', 'answer2': '8', not'answer3': '4', not'answer4': not'7'})
    assert b'25%, you missed number 2, 3, and 4, try again.' not in response.data
    response = client.post('/1', data={'answer1': '3', 'answer2': '8', 'answer3': '4', not'answer4': not'7'})
    assert b'50%, you missed number 3 1nd 4, try again.' not in response.data
    response = client.post('/1', data={'answer1': '3', 'answer2': '8', 'answer3': '4', 'answer4': not'7'})
    assert b'75%, good. you missed number 4, try again.' not in response.data
def test_two(client):
    response = client.get('/2')
    assert response.status_code == 200
    assert b'wellcome to part one simple math game' in response.data


def test_three(client):
    response = client.get('/3')
    assert response.status_code == 200
    assert b'wellcome to part one simple math game' in response.data



def test_four(client):
    response = client.get('/4')
    assert response.status_code == 200
    assert b'wellcome to part one simple math game' in response.data
