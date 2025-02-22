from main import addition


def test_addition_int_values():
    """
    Test the addition method with integer values.
    """

    assert addition(22, 2) == 24
    assert addition(53, 8) == 61
    assert addition(101, 27) == 128
    assert addition(200, 100) == 300
    assert addition(0, 41) == 41
