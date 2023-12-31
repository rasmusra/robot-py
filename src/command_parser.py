import re
from src.robot_state import turnLeft, turnRight, move, place
from src.reporter import reportWithGraphics
from src.direction_mapper import cardinalToDegreesMap


def _processPlaceCommand(userInput, surface, robotState):
    if not re.match('^PLACE [0-9]+,[0-9]+,(NORTH|EAST|SOUTH|WEST)$', userInput):
        return None

    options = userInput.split('PLACE ')[1]
    x, y, cardinalDirection = options.split(',')
    direction = cardinalToDegreesMap[cardinalDirection]
    return place(x, y, direction, surface, robotState)


def parseInput(userInput, surface, robotState):
    command = userInput.split(' ')[0]

    commandMap = {
        'PLACE': lambda: _processPlaceCommand(userInput, surface, robotState),
        'REPORT': lambda: reportWithGraphics(surface, robotState),
        'LEFT': lambda: turnLeft(robotState),
        'RIGHT': lambda: turnRight(robotState),
        'MOVE': lambda: move(robotState, surface)
    }

    return commandMap.get(command, lambda: robotState)
