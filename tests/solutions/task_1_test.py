import pytest
from solutions.task_1 import solve

test_cases = [
    (1, 5, 1, 10),
    (1, 5, 42, 420),
    (2, 5, 6, 30),
    (2, 3, 7, 21),   # lifehack is possible
    (2, 5, 5, 25),   # lifehack is possible
    (3, 10, 7, 50),  # lifehack is still possible
    (3, 10, 8, 60),  # lifehack is now not possible
    (4, 10, 15, 80),  # lifehack not possible
]


@pytest.mark.parametrize("k,m,n,exp", test_cases)
def test_task_1(k, m, n, exp):
    assert solve(k, m, n) == exp
