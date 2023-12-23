from src.robot_state import RobotState, turnLeft, turnRight, move
from src.tabletop import Tabletop


def test_createRobot():
    robotState = RobotState(1, 2, 0)
    assert robotState.x_position == 1
    assert robotState.y_position == 2
    assert robotState.direction == 0


def test_turnLeft():
    robotState = RobotState(1, 2, 0)
    robotState = turnLeft(robotState)
    assert robotState.direction == 270
    robotState = turnLeft(robotState)
    assert robotState.direction == 180
    robotState = turnLeft(robotState)
    assert robotState.direction == 90
    robotState = turnLeft(robotState)
    assert robotState.direction == 0


def test_turnRight():
    robotState = RobotState(1, 2, 0)
    robotState = turnRight(robotState)
    assert robotState.direction == 90
    robotState = turnRight(robotState)
    assert robotState.direction == 180
    robotState = turnRight(robotState)
    assert robotState.direction == 270
    robotState = turnRight(robotState)
    assert robotState.direction == 0


def test_move():
    robotState = RobotState(1, 2, 0)
    tabletop = Tabletop(5, 5)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 1
    assert robotState.y_position == 3
    robotState = turnRight(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 2
    assert robotState.y_position == 3
    robotState = turnRight(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 2
    assert robotState.y_position == 2
    robotState = turnRight(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 1
    assert robotState.y_position == 2
    robotState = turnRight(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 1
    assert robotState.y_position == 3
    robotState = turnLeft(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 0
    assert robotState.y_position == 3
    robotState = turnLeft(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 0
    assert robotState.y_position == 2
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 0
    assert robotState.y_position == 1
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 0
    assert robotState.y_position == 0
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 0
    assert robotState.y_position == 0
    robotState = turnRight(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 0
    assert robotState.y_position == 0
    robotState = turnLeft(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 0
    assert robotState.y_position == 0
    robotState = turnLeft(robotState)
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 1
    assert robotState.y_position == 0
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 2
    assert robotState.y_position == 0
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 3
    assert robotState.y_position == 0
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 4
    assert robotState.y_position == 0
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 4
    assert robotState.y_position == 0
    robotState = move(robotState, tabletop)
    assert robotState.x_position == 4
    assert robotState.y_position == 0
