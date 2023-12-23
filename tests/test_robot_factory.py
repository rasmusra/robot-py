import pytest
from src.robot_factory import tryCreate
from src.tabletop import Tabletop


@pytest.mark.parametrize('givenInstruction, expectedDirection',
                        [('PLACE 1,2,NORTH', 0),
                         ('PLACE 1,2,EAST', 90),
                         ('PLACE 1,2,SOUTH', 180),
                         ('PLACE 1,2,WEST', 270)])
def test_createRobot(givenInstruction, expectedDirection):
    robot = tryCreate(givenInstruction, Tabletop(2,3))
    assert robot.x_position == 1
    assert robot.y_position == 2
    assert robot.direction == expectedDirection

@pytest.mark.parametrize('givenFaultyInstruction',
                        [('PLACE -1,2,NORTH'),
                         ('PLACE 1,5,EAST'),
                         ('PLACE 1,2,SOTH'),
                         ('PLAC 1,2,WEST')])
def test_failCreatingRobot(givenFaultyInstruction):
    robot = tryCreate(givenFaultyInstruction, Tabletop(2,3))
    assert robot is None
