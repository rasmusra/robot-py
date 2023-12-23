from src.tabletop import Tabletop


def test_onBoard():
    tabletop = Tabletop(5, 5)
    assert tabletop.onBoard(0, 0) is True
    assert tabletop.onBoard(1, 1) is True
    assert tabletop.onBoard(4, 4) is True
    assert tabletop.onBoard(-1, -1) is False
    assert tabletop.onBoard(-1, 0) is False
    assert tabletop.onBoard(0, -1) is False
    assert tabletop.onBoard(0, 5) is False
    assert tabletop.onBoard(5, 0) is False
    assert tabletop.onBoard(5, 4) is False
    assert tabletop.onBoard(4, 5) is False
