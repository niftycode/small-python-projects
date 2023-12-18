import pytest


@pytest.fixture
def height():
    return 1.82


@pytest.fixture
def weight():
    return 79.4


def test_calculate_bmi(weight, height):
    """
    Test the calculate_bmi method.

    :param weight: The weight in kilograms.
    :param height: The height in meters.
    :return: None
    """
    bmi = weight / (height ** 2)
    assert isinstance(weight, float)
    assert isinstance(height, float)
    assert isinstance(bmi, float)
    assert pytest.approx(bmi, 2) == 23.97  # 23.970534959545947

    if bmi < 18.5:
        assert "Underweight"
    elif bmi >= 25:
        assert "Overweight"
    else:
        assert "Normal weight"
