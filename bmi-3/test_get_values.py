from unittest.mock import patch
from get_values import get_values


def test_get_values_valid_input():
    with patch("builtins.input", side_effect=["70", "1.75"]):
        weight, height = get_values()
        assert weight == 70.0
        assert height == 1.75


def test_get_values_invalid_weight_then_valid():
    with patch("builtins.input", side_effect=["invalid", "70", "1.75"]):
        weight, height = get_values()
        assert weight == 70.0
        assert height == 1.75


def test_get_values_invalid_height_then_valid():
    with patch("builtins.input", side_effect=["70", "invalid", "1.75"]):
        weight, height = get_values()
        assert weight == 70.0
        assert height == 1.75


def test_get_values_invalid_weight_and_height_then_valid():
    with patch("builtins.input", side_effect=["invalid", "70", "invalid", "1.75"]):
        weight, height = get_values()
        assert weight == 70.0
        assert height == 1.75
