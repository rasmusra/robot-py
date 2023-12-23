from src.robot import Robot
from src.tabletop import Tabletop


def test_createRobot():
    robot = Robot(1,2,0)
    assert robot.x_position == 1
    assert robot.y_position == 2
    assert robot.direction == 0

def test_turnLeft():
    robot = Robot(1,2,0)
    robot.turnLeft()
    assert robot.direction == 270
    robot.turnLeft()
    assert robot.direction == 180
    robot.turnLeft()
    assert robot.direction == 90
    robot.turnLeft()
    assert robot.direction == 0

def test_turnRight():
    robot = Robot(1,2,0)
    robot.turnRight()
    assert robot.direction == 90
    robot.turnRight()
    assert robot.direction == 180
    robot.turnRight()
    assert robot.direction == 270
    robot.turnRight()
    assert robot.direction == 0

def test_move():
    robot = Robot(1,2,0)
    tabletop = Tabletop(5,5)
    robot.move(tabletop)
    assert robot.x_position == 1
    assert robot.y_position == 3
    robot.turnRight()
    robot.move(tabletop)
    assert robot.x_position == 2
    assert robot.y_position == 3
    robot.turnRight()
    robot.move(tabletop)
    assert robot.x_position == 2
    assert robot.y_position == 2
    robot.turnRight()
    robot.move(tabletop)
    assert robot.x_position == 1
    assert robot.y_position == 2
    robot.turnRight()
    robot.move(tabletop)
    assert robot.x_position == 1
    assert robot.y_position == 3
    robot.turnLeft()
    robot.move(tabletop)
    assert robot.x_position == 0
    assert robot.y_position == 3
    robot.turnLeft()
    robot.move(tabletop)
    assert robot.x_position == 0
    assert robot.y_position == 2
    robot.move(tabletop)
    assert robot.x_position == 0
    assert robot.y_position == 1
    robot.move(tabletop)
    assert robot.x_position == 0
    assert robot.y_position == 0
    robot.move(tabletop)
    assert robot.x_position == 0
    assert robot.y_position == 0
    robot.turnRight()
    robot.move(tabletop)
    assert robot.x_position == 0
    assert robot.y_position == 0
    robot.turnLeft()
    robot.move(tabletop)
    assert robot.x_position == 0
    assert robot.y_position == 0
    robot.turnLeft()
    robot.move(tabletop)
    assert robot.x_position == 1
    assert robot.y_position == 0
    robot.move(tabletop)
    assert robot.x_position == 2
    assert robot.y_position == 0
    robot.move(tabletop)
    assert robot.x_position == 3
    assert robot.y_position == 0
    robot.move(tabletop)
    assert robot.x_position == 4
    assert robot.y_position == 0
    robot.move(tabletop)
    assert robot.x_position == 4
    assert robot.y_position == 0
    robot.move(tabletop)
    assert robot.x_position == 4
    assert robot.y_position == 0
