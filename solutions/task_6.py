def solve(a, b, c):
    # compute the discriminant
    d = b**2 - 4*a*c

    output = ""
    # only if d is non-negative we can take the square root
    if d >= 0:
        # compute roots according to the quadratic equation formula
        x1 = (-b + d**0.5)/(2*a)
        output += str(x1)
        # only add the second root if
        # the discriminant is not equal to 0
        # since otherwise the two roots are equal
        if d != 0:
            x2 = (-b - d**0.5)/(2*a)
            output += ' ' + str(x2)

    return output


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve(a, b, c))
