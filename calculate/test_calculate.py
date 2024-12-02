import pytest


@pytest.fixture
def number_one():
    return 30


@pytest.fixture
def number_two():
    return 15


def test_add(number_one, number_two):
    assert 45


def test_subtract(number_one, number_two):
    assert 15


def test_multiply(number_one, number_two):
    assert 450


def test_divide(number_one, number_two):
    assert 2
