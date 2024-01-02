import math


class RobotState:
    def __init__(self, x, y, direction):
        self.x = int(x)
        self.y = int(y)
        self.direction = int(direction)


def place(x, y, direction, surface, oldRobotState):
    if surface.onBoard(int(x), int(y)):
        return RobotState(int(x), int(y), direction)
    else:
        return oldRobotState


def turnLeft(robotState):
    if robotState is None:
        return None

    return RobotState(robotState.x, robotState.y,
                      (robotState.direction - 90) % 360)


def turnRight(robotState):
    if robotState is None:
        return None

    return RobotState(robotState.x, robotState.y,
                      (robotState.direction + 90) % 360)


def move(robotState, surface):
    if robotState is None:
        return None

    x_delta = round(math.sin(math.radians(robotState.direction)))
    y_delta = round(math.cos(math.radians(robotState.direction)))

    x = max(0, min(surface.width-1, robotState.x + x_delta))
    y = max(0, min(surface.width-1, robotState.y + y_delta))

    return RobotState(x, y, robotState.direction)
