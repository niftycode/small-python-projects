from main import BoxCalculator


def test_field_access():
    box = BoxCalculator(1, 2, 3)
    assert box.length == 1
    assert box.width == 2
    assert box.height == 3


def test_inequality():
    box1 = BoxCalculator(1, 2, 3)
    box2 = BoxCalculator(2, 3, 4)
    assert box1 != box2


def test_equality_with_different_ids():
    box1 = BoxCalculator(1, 2, 3)
    box2 = BoxCalculator(1, 2, 3)
    assert box1 is not box2


def test_calculate_volume():
    box = BoxCalculator(2, 3, 4)
    assert box.calculate_volume() == 24
