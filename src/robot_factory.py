from src.robot_state import RobotState
from src.directionMapper import cardinalToDegreesMap


def create(instruction, surface):
    robotState = None

    try:
        dataPart = instruction.split('PLACE ')[1]
        x_position, y_position, cardinalDirection = dataPart.split(',')
        direction = cardinalToDegreesMap[cardinalDirection]

        if surface.onBoard(int(x_position), int(y_position)):
            robotState = RobotState(int(x_position), int(y_position),
                                    direction)

    except Exception:
        robotState = None

    return robotState
