class Surface:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def onBoard(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height
