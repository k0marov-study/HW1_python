a = int(input())
b = int(input())

if a == 0:
    print("INF" if b == 0 else "NO")
elif b % a == 0:
    print(-b//a)
else:
    print("NO")
