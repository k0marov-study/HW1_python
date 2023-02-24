def solve(k, m, n):
    full_time = n//k * 2*m
    if n < k:
        full_time += 2*m
    elif n % k != 0:
        full_time += m if 2*(n % k) <= k else 2*m
    return full_time


if __name__ == '__main__':
    k = int(input())
    m = int(input())
    n = int(input())
    print(solve(k, m, n))
