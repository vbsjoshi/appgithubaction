from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(1,-4) == -3
    assert add(4,4) == 8
    assert add(0,0) == 0

def test_sub():
    assert sub(1,2) == -1
    assert sub(4,3) == 1
    assert sub(5,5) == 0
    assert sub(3,-5) == -2

