import pytest

from src.robot import Robot
from src.point import Point
from src.table import Table

@pytest.fixture
def mock_robot():
    mock_robot = Robot(
        table=Table(Point(0,0), Point(4,4)),
        movements={
            "north": Point(0,1),
            "east": Point(1,0),
            "south": Point(0,-1),
            "west": Point(-1,0),
        }
    )
    return mock_robot

def test_place_function(mock_robot):
    mock_robot.place(Point(1,1),"north")
    assert mock_robot.position.x == 1
    assert mock_robot.position.y == 1

def test_place_function_off_table(mock_robot):
    mock_robot.place(Point(1,3),"north")
    mock_robot.place(Point(5,5),"north")
    assert mock_robot.position.x == 1
    assert mock_robot.position.y == 3
    
def test_left_function(mock_robot):
    mock_robot.place(Point(1,1),"east")
    mock_robot.left()
    assert mock_robot.get_orientation() == "north"

def test_left_function_wrap_around(mock_robot):
    mock_robot.place(Point(1,1),"north")
    mock_robot.left()
    assert mock_robot.get_orientation() == "west"

def test_right_function(mock_robot):
    mock_robot.place(Point(1,1),"east")
    mock_robot.right()
    assert mock_robot.get_orientation() == "south"

def test_right_function_wrap_around(mock_robot):
    mock_robot.place(Point(1,1),"west")
    mock_robot.right()
    assert mock_robot.get_orientation() == "north"

def test_move_function(mock_robot):
    # Move North
    mock_robot.place(Point(1,1),"north")
    mock_robot.move()
    assert mock_robot.position.x == 1
    assert mock_robot.position.y == 2
    
    # Move East
    mock_robot.place(Point(1,1),"east")
    mock_robot.move()
    assert mock_robot.position.x == 2
    assert mock_robot.position.y == 1
    
    # Move South
    mock_robot.place(Point(1,1),"south")
    mock_robot.move()
    assert mock_robot.position.x == 1
    assert mock_robot.position.y == 0
    
    # Move West
    mock_robot.place(Point(1,1),"west")
    mock_robot.move()
    assert mock_robot.position.x == 0
    assert mock_robot.position.y == 1

def test_move_function_does_allow_robot_to_fall(mock_robot):
    # Moving North
    mock_robot.place(Point(1,1),"north")
    mock_robot.move()
    mock_robot.move()
    mock_robot.move()
    mock_robot.move()
    assert mock_robot.position.x == 1
    assert mock_robot.position.y == 4

    # Moving East
    mock_robot.place(Point(1,1),"east")
    mock_robot.move()
    mock_robot.move()
    mock_robot.move()
    mock_robot.move()
    assert mock_robot.position.x == 4
    assert mock_robot.position.y == 1

    # Moving South
    mock_robot.place(Point(1,1),"south")
    mock_robot.move()
    mock_robot.move()
    assert mock_robot.position.x == 1
    assert mock_robot.position.y == 0

    # Moving West
    mock_robot.place(Point(1,1),"west")
    mock_robot.move()
    mock_robot.move()
    assert mock_robot.position.x == 0
    assert mock_robot.position.y == 1

def test_report(mock_robot):
    mock_robot.place(Point(3,4),"north")
    assert mock_robot.report() == "I am currently at (3,4) facing NORTH"



