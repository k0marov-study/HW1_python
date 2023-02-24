import pytest
from solutions.task_3 import solve

test_cases = [
    (129, (0, 1, 2)),
    (61, (1, 0, 1)),
    (72, (2, 1, 1)),
    (25, (5, 2, 0)),
    (6,  (6, 0, 0)),
    (35, (0, 0, 1)),
    (36, (0, 0, 1)),
    (95, (0, 0, 2)),
    (96, (0, 0, 2)),
    (9,  (0, 1, 0)),
    (10, (0, 1, 0)),
    (11, (1, 1, 0)),
    (69, (0, 1, 1)),
    (19, (0, 2, 0)),
    (79, (0, 2, 1)),
    (500, (0, 2, 8)),
]


@pytest.mark.parametrize("n,exp", test_cases)
def test_task_3(n, exp):
    assert solve(n) == exp
