"""
Just write out the different forms of the word
for different values for n.

It turns out, that the cases for 10 <= n <= 20
are unique - the form is always "korov"

In other cases, the form depends on the last digit,
as written in the program.
"""


n = int(input())
word = ""
if 10 <= n <= 20 or n % 10 == 0 or 5 <= n % 10 <= 9:
    word = "korov"
elif n % 10 == 1:
    word = "korova"
else:
    word = "korovy"
print(n, word)
