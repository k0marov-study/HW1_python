def solve(a, b):
    if a == 0:
        return "INF" if b == 0 else "NO"
    elif b % a == 0:
        return str(-b//a)
    else:
        return "NO"


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(solve(a, b))
