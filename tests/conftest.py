import pytest

from tests.types import FixtureFunctionT


@pytest.fixture(scope='session', autouse=True)
def _init_db() -> FixtureFunctionT:
    print('start db')
    yield
    print('drop db')


@pytest.fixture()
def _void() -> FixtureFunctionT:
    print('hello void')
    yield
    print('hello after void')


@pytest.fixture()
def _void1() -> FixtureFunctionT:
    print('hello void1')
    return


@pytest.fixture()
def _void_group1(_void1, _void) -> FixtureFunctionT:
    print('void_group1')
    return


@pytest.fixture()
def a() -> int:
    yield 1


@pytest.fixture()
def b() -> int:
    return 2


NAMESPACE = {
    'a': 1,
    'b': 2
}
