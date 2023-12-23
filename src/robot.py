direction_graphics = {
    0: '⇑',
    90: '⇒',
    180: '⇓',
    270: '⇐' 
}

class Robot:
    def __init__(self, x_position, y_position, direction):
        self.x_position = int(x_position)
        self.y_position = int(y_position)
        self.direction = int(direction)
        
    def turnLeft(self):
        self.direction = (self.direction - 90) % 360

    def turnRight(self):
        self.direction = (self.direction + 90) % 360
        
    def move(self, tabletop):
        if self.direction == 0:
            self.y_position = min(tabletop.height-1, self.y_position + 1)
        elif self.direction == 90:
            self.x_position = min(tabletop.width-1, self.x_position + 1)
        elif self.direction == 180:
            self.y_position = max(0, self.y_position - 1)
        elif self.direction == 270:
            self.x_position = max(0, self.x_position - 1)
        else:
            raise Exception("Invalid robot: " + self.direction)

    def icon(self):
        return direction_graphics[self.direction]
