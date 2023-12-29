import re
from src.reporter import reportWithGraphics
from src.surface import Surface
from src.robot_state_factory import create
from src.robot_state import turnLeft, turnRight, move

surface = Surface(5, 5)
robotState = None

while robotState is None:
    userInput = input()
    robotState = create(userInput, surface)

while True:
    userInput = input()

    if userInput == 'REPORT':
        reportWithGraphics(surface, robotState)
        continue
    elif re.match('^PLACE', userInput):
        newRobotState = create(userInput, surface)
        robotState = newRobotState if newRobotState is not None else robotState
        continue
    elif userInput == 'LEFT':
        robotState = turnLeft(robotState)
        pass
    elif userInput == 'RIGHT':
        robotState = turnRight(robotState)
        pass
    elif userInput == 'MOVE':
        robotState = move(robotState, surface)
        pass
