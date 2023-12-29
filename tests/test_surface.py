from src.surface import Surface


def test_onBoard():
    surface = Surface(5, 5)
    assert surface.onBoard(0, 0) is True
    assert surface.onBoard(1, 1) is True
    assert surface.onBoard(4, 4) is True
    assert surface.onBoard(-1, -1) is False
    assert surface.onBoard(-1, 0) is False
    assert surface.onBoard(0, -1) is False
    assert surface.onBoard(0, 5) is False
    assert surface.onBoard(5, 0) is False
    assert surface.onBoard(5, 4) is False
    assert surface.onBoard(4, 5) is False
