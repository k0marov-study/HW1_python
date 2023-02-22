k = int(input())
m = int(input())
n = int(input())

full_time = 0
iteration_count = n//k
iteration_time = 2*m
full_time += iteration_count * iteration_time
if n < k:
    full_time += iteration_time
elif n % k != 0:
    full_time += m if 2*(n % k) <= k else 2 * m
print(full_time)
