arabic = int(input())
roman = ''

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

roman += 'X' * (arabic // 10)
arabic %= 10

if arabic == 9:
    roman += 'IX'
    arabic -= 9
if arabic == 4:
    roman += 'IV'
    arabic -= 4

if arabic >= 5:
    roman += 'V'
    arabic -= 5

roman += 'I'*arabic


print(roman)
