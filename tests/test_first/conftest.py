import pytest


@pytest.fixture()
def test_first_fixture(_void_group1: None) -> None:
    print('test_first_fixture')

