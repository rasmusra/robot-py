from src.robot_state import RobotState
from src.directionMapper import cardinalToDegreesMap

def tryCreate(instruction, tabletop):
    robotState = None

    try:
        dataPart = instruction.split('PLACE ')[1]
        x_position, y_position, cardinalDirection = dataPart.split(',')
        direction = cardinalToDegreesMap[cardinalDirection]

        if tabletop.onBoard(int(x_position), int(y_position)):
            robotState = RobotState(int(x_position), int(y_position), direction)

    except:
        pass

    return robotState
