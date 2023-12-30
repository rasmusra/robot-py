import re
from src.robot_state import turnLeft, turnRight, move, place
from src.reporter import reportWithGraphics
from src.direction_mapper import cardinalToDegreesMap


def _parsePlaceCommand(instruction, surface):
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


def parseCommand(userInput, surface, robotState):
    if userInput == 'REPORT':
        return reportWithGraphics(surface, robotState)
    elif re.match('^PLACE', userInput):
        newRobotState = _parsePlaceCommand(userInput, surface)
        return robotState if newRobotState is None else newRobotState
    elif userInput == 'LEFT':
        return turnLeft(robotState)
    elif userInput == 'RIGHT':
        return turnRight(robotState)
    elif userInput == 'MOVE':
        return move(robotState, surface)
    else:
        return robotState
