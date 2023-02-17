import pytest
from solutions.task_5 import solve

test_cases = [
        (0, 0, "INF"),
        (0, 5, "NO"),
        (1, 0, "0"),
        (5, 5, "-1"),
        (4, 2, "NO"),
        (2, 4, "-2"),
        (2, -4, "2"),
        (-2, 4, "2"),
        (3, 6, "-2"),
        (3, 8, "NO"),
]

@pytest.mark.parametrize("a,b,expected", test_cases)
def test_task_2(a, b, expected):
    result = solve(a, b)
    assert result == expected
