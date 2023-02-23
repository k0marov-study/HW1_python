import pytest
from solutions.task_2 import solve

test_cases = [
    (1, 1, 1, 1, "YES"),
    (-1, -1, -1, -1, "YES"),
    (-1, 1, -2, 2, "YES"),
    (42, 33, 15, 56, "YES"),
    (-33, 22, 33, -2, "NO"),
    (55, 55, -2, -3, "NO"),
    (42, -3, 3, 3, "NO"),
    (-10, -300, -10, 55, "NO"),
]


@pytest.mark.parametrize("x1,y1,x2,y2,expected", test_cases)
def test_task_2(x1, y1, x2, y2, expected):
    result = solve(x1, y1, x2, y2)
    assert result == expected
