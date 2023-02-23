def solve(x1, y1, x2, y2):
    same_quarter = (x1 > 0) == (x2 > 0) and (y1 > 0) == (y2 > 0)

    return "YES" if same_quarter else "NO"


if __name__ == '__main__':
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    print(solve(x1, y1, x2, y2))
