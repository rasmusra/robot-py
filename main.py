import re
from src.reporter import reportWithGraphics
from src.tabletop import Tabletop
from src.robot_factory import tryCreate
from src.robot_state import turnLeft, turnRight, move

tabletop = Tabletop(5,5)
robotState = None

while robotState is None:
    userInput = input()
    robotState = tryCreate(userInput, tabletop)

while True:
    userInput = input()

    if userInput == 'REPORT':
        reportWithGraphics(tabletop, robotState)
        continue
    elif re.match('^PLACE', userInput):
        newRobotState = tryCreate(userInput, tabletop)
        robotState = newRobotState if newRobotState is not None else robotState
        continue
    elif userInput == 'LEFT':
        robotState = turnLeft(robotState)
        pass
    elif userInput == 'RIGHT':
        robotState = turnRight(robotState)
        pass
    elif userInput == 'MOVE':
        robotState = move(robotState, tabletop)
        pass
