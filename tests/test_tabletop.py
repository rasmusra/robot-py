from src.tabletop import Tabletop


def test_onBoard():
    tabletop = Tabletop(5, 5)
    assert tabletop.onBoard(0, 0) == True
    assert tabletop.onBoard(1, 1) == True
    assert tabletop.onBoard(4, 4) == True
    assert tabletop.onBoard(-1, -1) == False
    assert tabletop.onBoard(-1, 0) == False
    assert tabletop.onBoard(0, -1) == False
    assert tabletop.onBoard(0, 5) == False
    assert tabletop.onBoard(5, 0) == False
    assert tabletop.onBoard(5, 4) == False
    assert tabletop.onBoard(4, 5) == False
    
    