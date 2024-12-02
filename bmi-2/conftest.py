import pytest

"""
This file is used by pytest. It is the configuration file
for tests. For example, common fixtures are defined here.
Unlike other Python files, conftest.py is automatically
detected and loaded by pytest.
"""


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
