from app.app import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False
    except ValueError:
        assert True


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("All tests passed successfully")
