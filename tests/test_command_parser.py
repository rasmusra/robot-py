import pytest
from src.command_parser import parseCommand
from src.surface import Surface


@pytest.mark.parametrize('userInput, expectedDirection',
                         [('PLACE 1,2,NORTH', 0),
                          ('PLACE 1,2,EAST', 90),
                          ('PLACE 1,2,SOUTH', 180),
                          ('PLACE 1,2,WEST', 270)])
def test_placeFirstRobot(userInput, expectedDirection):
    command = parseCommand(userInput, Surface(2, 3))
    robotState = command(None)
    assert robotState.x_position == 1
    assert robotState.y_position == 2
    assert robotState.direction == expectedDirection


@pytest.mark.parametrize('userInput, x, y, direction',
                         [('MOVE', 2, 2, 90),
                          ('LEFT', 1, 2, 0),
                          ('RIGHT', 1, 2, 180),
                          ('REPORT', 1, 2, 90)])
def test_operateRobot(userInput, x, y, direction):
    surface = Surface(5, 5)
    robotState = parseCommand('PLACE 1,2,EAST', surface)(None)
    command = parseCommand(userInput, surface)
    newRobotState = command(robotState)
    assert newRobotState.x_position == x
    assert newRobotState.y_position == y
    assert newRobotState.direction == direction


@pytest.mark.parametrize('givenFaultyInstruction',
                         [('PLACE -1,2,NORTH'),
                          ('PLACE 1,5,EAST'),
                          ('PLACE 1,2,SOTH'),
                          ('PLAC 1,2,WEST')])
def test_failCreatingFirstRobot(givenFaultyInstruction):
    command = parseCommand(givenFaultyInstruction, Surface(2, 3))
    robotState = command(None)
    assert robotState is None
