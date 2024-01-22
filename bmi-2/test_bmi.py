import pytest

from main import calculate_bmi


@pytest.fixture
def under_height():
    return 1.82


@pytest.fixture
def under_weight():
    return 79.4


def test_calculate_bmi_normal_weight(under_weight, under_height, capsys):
    calculate_bmi(under_weight, under_height)
    captured = capsys.readouterr()
    assert captured.out == "Normal weight\n"


@pytest.mark.skip(reason="no test available")
def test_calculate_bmi_overweight(weight, height):
    # TODO - 21.01.2024: Add more tests
    ...


@pytest.mark.skip(reason="no test available")
def test_calculate_bmi_underweight(weight, height):
    # TODO - 21.01.2024: Add more tests
    ...
