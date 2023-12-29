import math

class RobotState:
    def __init__(self, x_position, y_position, direction):
        self.x_position = int(x_position)
        self.y_position = int(y_position)
        self.direction = int(direction)


def place(x_position, y_position, direction, surface):
    if surface.onBoard(int(x_position), int(y_position)):
        return RobotState(int(x_position), int(y_position), direction)
    else:
        return None


def turnLeft(robotState):
    if robotState is None:
        return None
    
    return RobotState(robotState.x_position, robotState.y_position,
                      (robotState.direction - 90) % 360)


def turnRight(robotState):
    if robotState is None:
        return None
    
    return RobotState(robotState.x_position, robotState.y_position,
                      (robotState.direction + 90) % 360)


def move(robotState, surface):
    if robotState is None:
        return None
    
    x_delta = round(math.sin(math.radians(robotState.direction)))
    y_delta = round(math.cos(math.radians(robotState.direction)))

    x_position = max(0, min(surface.width-1, robotState.x_position + x_delta))
    y_position = max(0, min(surface.width-1, robotState.y_position + y_delta))

    return RobotState(x_position, y_position, robotState.direction)
