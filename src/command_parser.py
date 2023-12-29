import re
from src.robot_state import turnLeft, turnRight, move, place
from src.reporter import reportWithGraphics
from src.direction_mapper import cardinalToDegreesMap


def _create(instruction, surface):
    robotState = None

    try:
        dataPart = instruction.split('PLACE ')[1]
        x_position, y_position, cardinalDirection = dataPart.split(',')
        direction = cardinalToDegreesMap[cardinalDirection]
        robotState = place(int(x_position), int(y_position), direction, 
                           surface)

    except Exception:
        robotState = None

    return robotState


def parseCommand(userInput, surface):
    if userInput == 'REPORT':
        return lambda robotState: reportWithGraphics(surface, robotState)
    elif re.match('^PLACE', userInput):
        newRobotState = _create(userInput, surface)
        return lambda robotState: robotState if newRobotState is None else newRobotState 
    elif userInput == 'LEFT':
        return lambda robotState: turnLeft(robotState)
    elif userInput == 'RIGHT':
        return lambda robotState: turnRight(robotState)
    elif userInput == 'MOVE':
        return lambda robotState: move(robotState, surface)
    else:
        return lambda robotState: robotState
