import pytest
from solutions.task_8 import solve

test_cases = [
    (5, 1, 1, 1, "1 2"),
    (5, 1, 1, 2, "1 1"),
    (5, 6, 1, 1, "-1"),    # k > n
    (6, 6, 1, 1, "-1"),   # k == n
    (10, 3, 3, 1, "4 2"),
    (11, 3, 5, 1, "3 2"),  # a student cannot sit alone on the second place
    (10, 2, 3, 1, "4 1"),  # behind is preferred to in-front
    (10, 2, 5, 1, "4 1"),  # behind is impossible
    (10, 2, 1, 2, "2 2"),  # before is impossible
]


@pytest.mark.parametrize("n,k,row,place,exp", test_cases)
def test_task_8(n, k, row, place, exp):
    assert solve(n, k, row, place) == exp
