from calculator import average

def test_average():
    assert average([1, 2, 3, 4, 5]) == 5.0
    
    assert average([-1, -2, -3, -4, -5]) == -3.0
    
    assert average([1.5, 2.5, 3.5, 4.5, 5.5]) == 3.5
    
    assert average([10]) == 10.0

    try:
        average([])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for empty list"
