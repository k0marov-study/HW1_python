SMALL = 1
MIDDLE = 10
BIG = 60

BIG_CHEAPER_MIDDLE = 35
MIDDLE_CHEAPER_SMALL = 9

n = int(input())

big_amount = n // BIG
n %= BIG

if n >= BIG_CHEAPER_MIDDLE:
    n = 0
    big_amount += 1

middle_amount = n // MIDDLE
n %= MIDDLE

if n >= MIDDLE_CHEAPER_SMALL:
    n = 0
    middle_amount += 1

small_amount = n

print(small_amount, middle_amount, big_amount)
