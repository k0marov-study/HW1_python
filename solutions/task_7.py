"""
Just write out the different forms of the word
for different values for n.

It turns out, that the cases for 10 <= n <= 20
are unique - the form is always "korov"

In other cases, the form depends on the last digit,
as written in the program.
"""


def solve(n):
    word = ""
    if 10 <= n <= 20 or n % 10 == 0 or 5 <= n % 10 <= 9:
        word = "korov"
    elif n % 10 == 1:
        word = "korova"
    else:
        word = "korovy"
    return f"{n} {word}"


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
