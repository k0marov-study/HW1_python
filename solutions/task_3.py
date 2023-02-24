SMALL = 1
MIDDLE = 10
BIG = 60
BIG_CHEAPER_MIDDLE = 35
MIDDLE_CHEAPER_SMALL = 9


def solve(n):
    big_amount = n // BIG
    n %= BIG
    if n >= BIG_CHEAPER_MIDDLE:
        return 0, 0, big_amount+1

    middle_amount = n // MIDDLE
    n %= MIDDLE
    if n >= MIDDLE_CHEAPER_SMALL:
        return 0, middle_amount+1, big_amount

    small_amount = n
    return small_amount, middle_amount, big_amount


if __name__ == '__main__':
    n = int(input())
    small, middle, big = solve(n)
    print(small, middle, big)
