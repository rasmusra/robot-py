from src.tabletop import Tabletop
from src.robot import Robot
from src.reporter import reportWithGraphics, reportData


def test_report_data(capsys):
    robot = Robot(2, 3, 0)
    
    reportData(robot)
    
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Robot is at position (2, 3) facing NORTH'

def test_report_with_graphics(capsys):
    tabletop = Tabletop(1, 1)
    robot = Robot(0, 0, 0)
    green = '\x1b[32m'
    white = '\x1b[0m'
    red = '\x1b[31m'

    reportWithGraphics(tabletop, robot)
    
    captured = capsys.readouterr()
    assert captured.out.strip() == f'''\
{green}---
|{red}⇑{green}|
---{white}\
'''