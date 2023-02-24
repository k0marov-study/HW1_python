def solve(a, b):
    if a == 0:
        # if the coefficient for x is equal to 0
        # then the expression does not depend on x
        # so there is either 0 answers - when b != 0,
        # or an infinite number of answers when b == 0,
        # since we can substitute any x into equation
        # 0 = 0
        # and it will be truthful
        return "INF" if b == 0 else "NO"
    elif b % a == 0:
        # because the equation needs to be solved
        # in integer values, there will be an answer only
        # if b divides into a without a remainder
        return str(-b//a)
    else:
        # otherwise, there is no answers
        return "NO"


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(solve(a, b))
