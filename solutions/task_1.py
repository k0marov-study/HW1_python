k = int(input())
m = int(input())
n = int(input())

full_time = n//k * 2*m
if n < k:
    full_time += 2*m
elif n % k != 0:
    full_time += m if 2*(n % k) <= k else 2*m
print(full_time)
