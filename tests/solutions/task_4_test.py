import pytest
import roman
from solutions.task_4 import solve

test_cases = [
    (n, roman.toRoman(n))
    for n in range(1, 100)
]


@pytest.mark.parametrize("arabic,roman", test_cases)
def test_task_4(arabic, roman):
    assert solve(arabic) == roman
