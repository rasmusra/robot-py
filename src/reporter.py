from src.directionMapper import degreesToCardinalMap


fgColor = {
    'green': '\x1b[32m',
    'white': '\x1b[0m',
    'red': '\x1b[31m'
}


direction_graphics = {
    0: '⇑',
    90: '⇒',
    180: '⇓',
    270: '⇐'
}


def reportWithGraphics(tabletop, robotState):
    verticalBorder = '-' * (tabletop.width+2)
    emptyCells = '|' + ' ' * tabletop.width + '|'
    cellsBeforeRobot = '|' + ' ' * robotState.x_position
    robotIcon = direction_graphics[robotState.direction]
    robot = fgColor['red'] + robotIcon + fgColor['green']
    numberOfCellsAfterRobot = tabletop.width - robotState.x_position - 1
    cellsAfterRobot = ' ' * numberOfCellsAfterRobot + '|'
    numberOfLinesAboveRobot = tabletop.height-1 - robotState.y_position

    print(fgColor['green'] + verticalBorder)
    [print(emptyCells) for line in range(numberOfLinesAboveRobot)]
    print(cellsBeforeRobot + robot + cellsAfterRobot)
    [print(emptyCells) for line in range(robotState.y_position)]
    print(verticalBorder + fgColor['white'])


def reportData(robot):
    print(f'Robot is at position ({robot.x_position}, {robot.y_position})\
 facing {degreesToCardinalMap(robot.direction)}')
