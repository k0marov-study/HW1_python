import pytest
from solutions.task_7 import solve

test_cases = [
    (1, "1 korova"),
    (2, "2 korovy"),
    (5, "5 korov"),
    (10, "10 korov"),
    (12, "12 korov"),
    (19, "19 korov"),
    (20, "20 korov"),
    (30, "30 korov"),
    (42, "42 korovy"),
    (46, "46 korov"),
    (87, "87 korov"),
    (88, "88 korov"),
    (99, "99 korov"),
    (94, "94 korovy"),
    (99, "99 korov"),
]


@pytest.mark.parametrize("n,exp", test_cases)
def test_task_7(n, exp):
    assert solve(n) == exp
