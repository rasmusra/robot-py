from src.surface import Surface
from src.command_parser import parseInput

surface = Surface(5, 5)
robotState = None

while True:
    try:
        userInput = input()
        robotState = parseInput(userInput, surface, robotState)()
    except KeyboardInterrupt:
        print('\n')
        exit()
