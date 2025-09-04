import pytest
from Robot import Robot 

def test_init_defaults():
    r = Robot()
    assert r.status == (0, 0, "N")

def test_turn_left():
    r = Robot()
    r.turnLeft()
    assert r.status == (0, 0, "W")

def test_turn_right():
    r = Robot()
    r.turnRight()
    assert r.status == (0, 0, "E")

def test_move_forward():
    r = Robot()
    r.moveForward()
    assert r.status == (0, 1, "N")

