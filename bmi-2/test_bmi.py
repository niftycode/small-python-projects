import pytest

from main import calculate_bmi


@pytest.fixture
def under_height():
    return 1.82


@pytest.fixture
def under_weight():
    return 59.0


@pytest.fixture
def normal_height():
    return 1.82


@pytest.fixture
def normal_weight():
    return 79.6


@pytest.fixture
def over_height():
    return 1.82


@pytest.fixture
def over_weight():
    return 101.0


def test_calculate_bmi_under_weight(under_weight, under_height, capsys):
    calculate_bmi(under_weight, under_height)
    captured = capsys.readouterr().out.rstrip()
    assert captured == "Underweight"


# @pytest.mark.skip(reason="no test available")
def test_calculate_bmi_normal_weight(normal_weight, normal_height, capsys):
    calculate_bmi(normal_weight, normal_height)
    captured = capsys.readouterr().out.rstrip()
    assert captured == "Normal weight"


def test_calculate_bmi_overweight(over_weight, over_height, capsys):
    calculate_bmi(over_weight, over_height)
    captured = capsys.readouterr().out.rstrip()
    assert captured == "Overweight"
