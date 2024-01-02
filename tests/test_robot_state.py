from src.robot_state import RobotState, turnLeft, turnRight, move, place
from src.surface import Surface


def test_place():
    surface = Surface(3, 3)
    robotState = place(1, 2, 90, surface, None)
    assert robotState is not None


def test_failPace():
    surface = Surface(3, 3)
    oldRobotState = RobotState(1, 2, 90)
    robotState = place(1, 3, 90, surface, oldRobotState)
    assert robotState is oldRobotState


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
    surface = Surface(5, 5)
    robotState = move(robotState, surface)
    assert robotState.x_position == 1
    assert robotState.y_position == 3
    robotState = turnRight(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 2
    assert robotState.y_position == 3
    robotState = turnRight(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 2
    assert robotState.y_position == 2
    robotState = turnRight(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 1
    assert robotState.y_position == 2
    robotState = turnRight(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 1
    assert robotState.y_position == 3
    robotState = turnLeft(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 0
    assert robotState.y_position == 3
    robotState = turnLeft(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 0
    assert robotState.y_position == 2
    robotState = move(robotState, surface)
    assert robotState.x_position == 0
    assert robotState.y_position == 1
    robotState = move(robotState, surface)
    assert robotState.x_position == 0
    assert robotState.y_position == 0
    robotState = move(robotState, surface)
    assert robotState.x_position == 0
    assert robotState.y_position == 0
    robotState = turnRight(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 0
    assert robotState.y_position == 0
    robotState = turnLeft(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 0
    assert robotState.y_position == 0
    robotState = turnLeft(robotState)
    robotState = move(robotState, surface)
    assert robotState.x_position == 1
    assert robotState.y_position == 0
    robotState = move(robotState, surface)
    assert robotState.x_position == 2
    assert robotState.y_position == 0
    robotState = move(robotState, surface)
    assert robotState.x_position == 3
    assert robotState.y_position == 0
    robotState = move(robotState, surface)
    assert robotState.x_position == 4
    assert robotState.y_position == 0
    robotState = move(robotState, surface)
    assert robotState.x_position == 4
    assert robotState.y_position == 0
    robotState = move(robotState, surface)
    assert robotState.x_position == 4
    assert robotState.y_position == 0
