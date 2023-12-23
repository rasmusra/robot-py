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
    if robotState.direction == 0:
        return RobotState(robotState.x_position,
                          min(tabletop.height-1, robotState.y_position + 1),
                          robotState.direction)
    elif robotState.direction == 90:
        return RobotState(min(tabletop.width-1, robotState.x_position + 1),
                          robotState.y_position,
                          robotState.direction)
    elif robotState.direction == 180:
        return RobotState(robotState.x_position,
                          max(0, robotState.y_position - 1),
                          robotState.direction)
    elif robotState.direction == 270:
        return RobotState(max(0, robotState.x_position - 1),
                          robotState.y_position,
                          robotState.direction)
    else:
        raise Exception("Invalid robot: " + robotState.direction)
