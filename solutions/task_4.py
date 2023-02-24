arabic = int(input())
roman = ''

# At first, we just treat C and L as prefixes
# that subtract the respective value from arabic
# But we also have two special cases (the subtractive notation):
# XC and XL, and we handle them separately
if arabic >= 100:
    roman += 'C'
    arabic -= 100
if arabic >= 90:
    roman += 'XC'
    arabic -= 90
if arabic >= 50:
    roman += 'L'
    arabic -= 50
if arabic >= 40:
    roman += 'XL'
    arabic -= 40

# then it's easy to add as much 'X's as needed
# by getting the number of tens left in arabic
roman += 'X' * (arabic // 10)
arabic %= 10

# now arabic has a value from 0 to 9
# and we need to add it to Roman

# handle the special subtractive notation cases
if arabic == 9:
    roman += 'IX'
    arabic -= 9
if arabic == 4:
    roman += 'IV'
    arabic -= 4

# handle the case when there is more than 5 left
# since then we need to start with V
if arabic >= 5:
    roman += 'V'
    arabic -= 5

# add as much 'I' as there are ones left in arabic
roman += 'I'*arabic

print(roman)
