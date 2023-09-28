import pytest
from pytest_bdd import (
    scenario,
    scenarios,
    given,
    when,
    then,
    parser,
    parsers
)

scenarios('../')

@pytest.fixture()
def init():
    pass









