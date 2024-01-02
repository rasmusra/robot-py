import re
from src.robot_state import turnLeft, turnRight, move, place
from src.reporter import reportWithGraphics
from src.direction_mapper import cardinalToDegreesMap


def _parsePlaceCommand(instruction):
    if not re.match('^PLACE [0-9]+,[0-9]+,(NORTH|EAST|SOUTH|WEST)$', instruction):
        return None

    dataPart = instruction.split('PLACE ')[1]
    x_position, y_position, cardinalDirection = dataPart.split(',')
    direction = cardinalToDegreesMap[cardinalDirection]
    return int(x_position), int(y_position), direction


def _processPlaceCommand(userInput, surface, robotState):
    placeData = _parsePlaceCommand(userInput)
    if placeData is None:
        return None

    x, y, dir = placeData
    return place(x, y, dir, surface, robotState)


def parseCommand(userInput, surface, robotState):
    command = userInput.split(' ')[0]

    commandMap = {
        'PLACE': lambda: _processPlaceCommand(userInput, surface, robotState),
        'REPORT': lambda: reportWithGraphics(surface, robotState),
        'LEFT': lambda: turnLeft(robotState),
        'RIGHT': lambda: turnRight(robotState),
        'MOVE': lambda: move(robotState, surface)
    }

    return commandMap.get(command, lambda: robotState)
