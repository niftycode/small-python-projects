import pytest


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
