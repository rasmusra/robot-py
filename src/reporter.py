
from src.directionMapper import degreesToCardinalMap
# from simple_colors import green, red

fgColor = {
    'green': '\x1b[32m',
    'white': '\x1b[0m',
    'red': '\x1b[31m'
}

def reportWithGraphics(tabletop, robot):
    verticalBorder = '-' * (tabletop.width+2)
    emptyLine = '|' + ' ' * tabletop.width + '|'
    spacesBeforeRobot = '|' + ' ' * robot.x_position
    robotDisplay = fgColor['red'] + robot.icon() + fgColor['green']
    numberOfSpaceAfterRobot = tabletop.width-robot.x_position-1
    spacesAfterRobot = ' ' * numberOfSpaceAfterRobot + '|'
    numberOfLinesAboveRobot = tabletop.height-1 - robot.y_position

    print(fgColor['green'] + verticalBorder)
    [print(emptyLine) for line in range(numberOfLinesAboveRobot)]
    print(spacesBeforeRobot + robotDisplay + spacesAfterRobot)
    [print(emptyLine) for line in range(robot.y_position)]
    print(verticalBorder + fgColor['white'])

def reportData(robot):
    print(f'Robot is at position ({robot.x_position}, {robot.y_position})\
 facing {degreesToCardinalMap(robot.direction)}')
