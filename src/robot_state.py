import math

class RobotState:
    def __init__(self, x_position, y_position, direction):
        self.x_position = int(x_position)
        self.y_position = int(y_position)
        self.direction = int(direction)


def turnLeft(robotState):
    return RobotState(robotState.x_position, robotState.y_position,
                      (robotState.direction - 90) % 360)


def turnRight(robotState):
    return RobotState(robotState.x_position, robotState.y_position,
                      (robotState.direction + 90) % 360)


def move(robotState, tabletop):
    x_delta = round(math.sin(math.radians(robotState.direction)))
    y_delta = round(math.cos(math.radians(robotState.direction)))

    x_position = max(0, min(tabletop.width-1, robotState.x_position + x_delta))
    y_position = max(0, min(tabletop.width-1, robotState.y_position + y_delta))

    return RobotState(x_position, y_position, robotState.direction)
