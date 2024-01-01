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
    result = robotState

    commandMap = {
        'REPORT': lambda: reportWithGraphics(surface, robotState),
        'LEFT': lambda: turnLeft(robotState),
        'RIGHT': lambda: turnRight(robotState),
        'MOVE': lambda: move(robotState, surface)
    }

    if re.match('^PLACE', userInput):
        newRobotState = _parsePlaceCommand(userInput, surface)
        result = robotState if newRobotState is None else newRobotState
    else:
        result = commandMap.get(userInput, lambda: robotState)()

    return result
