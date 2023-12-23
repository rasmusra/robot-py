cardinalToDegreesMap = {
    'NORTH': 0,
    'EAST': 90,
    'SOUTH': 180,
    'WEST': 270
}

def degreesToCardinalMap(direction):
    for facing, d in cardinalToDegreesMap.items():
        if d == direction:
            return facing
