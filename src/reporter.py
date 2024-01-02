from src.direction_mapper import degreesToCardinalMap


fgColor = {
    'green': '\x1b[32m',
    'white': '\x1b[0m',
    'red': '\x1b[31m'
}


directionIcon = {
    0: '⇑',
    90: '⇒',
    180: '⇓',
    270: '⇐'
}


def reportWithGraphics(surface, robotState):
    if robotState is None:
        return None

    verticalBorder = '-' * (surface.width+2)
    emptyCells = '|' + ' ' * surface.width + '|'
    cellsBeforeRobot = '|' + ' ' * robotState.x
    robotIcon = directionIcon[robotState.direction]
    robot = fgColor['red'] + robotIcon + fgColor['green']
    numberOfCellsAfterRobot = surface.width - robotState.x - 1
    cellsAfterRobot = ' ' * numberOfCellsAfterRobot + '|'
    numberOfLinesAboveRobot = surface.height-1 - robotState.y

    print(fgColor['green'] + verticalBorder)
    [print(emptyCells) for _ in range(numberOfLinesAboveRobot)]
    print(cellsBeforeRobot + robot + cellsAfterRobot)
    [print(emptyCells) for _ in range(robotState.y)]
    print(verticalBorder + fgColor['white'])

    return robotState


def reportData(robotState):
    if robotState is None:
        return None

    print(f'Robot is at position ({robotState.x}, {robotState.y})\
 facing {degreesToCardinalMap(robotState.direction)}')

    return robotState
