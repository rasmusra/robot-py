from src.surface import Surface
from src.command_parser import parseCommand

surface = Surface(5, 5)
robotState = None

while True:
    userInput = input()
    command = parseCommand(userInput, surface)
    robotState = command(robotState)
