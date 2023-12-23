import re
from src.reporter import reportWithGraphics
from src.tabletop import Tabletop
from src.robot_factory import tryCreate

tabletop = Tabletop(5,5)
robot = None

while robot is None:
    userInput = input()
    robot = tryCreate(userInput, tabletop)

while True:
    userInput = input()

    if userInput == 'REPORT':
        reportWithGraphics(tabletop, robot)
        continue
    elif re.match('^PLACE', userInput):
        newRobot = tryCreate(userInput, tabletop)
        robot = newRobot if newRobot is not None else robot
        continue
    elif userInput == 'LEFT':
        robot.turnLeft()
        pass
    elif userInput == 'RIGHT':
        robot.turnRight()
        pass
    elif userInput == 'MOVE':
        robot.move(tabletop)
        pass
