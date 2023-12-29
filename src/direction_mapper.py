cardinalToDegreesMap = {
    'NORTH': 0,
    'EAST': 90,
    'SOUTH': 180,
    'WEST': 270
}


def degreesToCardinalMap(direction):
    for cardinal, degrees in cardinalToDegreesMap.items():
        if degrees == direction:
            return cardinal
