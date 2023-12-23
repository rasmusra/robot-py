from src.directionMapper import *

def test_cardinalToDegreesMap():
    actual = cardinalToDegreesMap["SOUTH"]
    assert 180 == actual

def test_degreesToCardinalMap():
    actual = degreesToCardinalMap(270)
    assert "WEST" == actual