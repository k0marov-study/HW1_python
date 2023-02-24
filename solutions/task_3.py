"""
Since 1-ticket price decreases with the total packet size inrease, 
the task is solved by getting as much big packets as possible
without getting more tickets than needed, 
and then repeating the same for middle and small packets. 

The only caveat is that it is actually cheaper to buy 
one big packet than middle and small ones for the case
when 35 <= n <= 60 (we can count that on paper). 
It is also cheaper to buy 1 middle packet for the case when 
n = 9  (we can also count that on paper).
So we need to handle these two cases separately. 
"""

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
