import pytest
from solutions.task_6 import solve

test_cases = [
    (1, 4, 4, "-2.0"),
    (1, -4, 4, "2.0"),
    (2, 8, 8, "-2.0"),
    (2, -8, 8, "2.0"),
    (1, 4, 3, "-1.0 -3.0"),
    (1, -4, 3, "3.0 1.0"),
    (1, -3.5, 2.5, "2.5 1.0"),
    (2, -7, 5, "2.5 1.0"),
    (1, 1, 5, ""),
    (5, 6, 4, ""),
    (1.5, 3, 3, ""),
]


@pytest.mark.parametrize("a,b,c,expected", test_cases)
def test_task_6(a, b, c, expected):
    assert solve(a, b, c) == expected
