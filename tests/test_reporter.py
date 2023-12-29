from src.surface import Surface
from src.robot_state import RobotState
from src.reporter import reportWithGraphics, reportData


def test_report_data(capsys):
    robotState = RobotState(2, 3, 0)

    reportData(robotState)

    captured = capsys.readouterr()
    assert captured.out.strip() == 'Robot is at position (2, 3) facing NORTH'


def test_report_with_graphics(capsys):
    surface = Surface(1, 1)
    robotState = RobotState(0, 0, 0)
    green = '\x1b[32m'
    white = '\x1b[0m'
    red = '\x1b[31m'

    reportWithGraphics(surface, robotState)

    captured = capsys.readouterr()
    assert captured.out.strip() == f'''\
{green}---
|{red}⇑{green}|
---{white}\
'''
