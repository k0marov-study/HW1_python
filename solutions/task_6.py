def solve(a, b, c):
    d = b**2 - 4*a*c

    output = ""
    if d >= 0:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        output += str(x1)
        if x2 != x1:
            output += ' ' + str(x2)

    return output


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve(a, b, c))
