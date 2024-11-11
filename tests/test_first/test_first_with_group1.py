import pytest


@pytest.mark.usefixtures("test_first_fixture")
@pytest.mark.parametrize(
    ('value', 'value1'),
    [
        (1, 2),
        (3, 4),
    ]
)
def test_first_with_group(
    a: int,
    b: int,
    value: int,
    value1: int,
) -> None:
    assert value == value1
    assert a == b
