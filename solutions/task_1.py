"""
For the cases when n divides into k the steps are simple - 
we just place as much food as possible and cook it from two sides. 
So the answer is n//k * 2*m, since there will be n / k iterations 
and for each we need to cook from two sides, hence 2*m.
We also need to add 2*m for the case when n < k, because the previous formula 
will give 0, but actually you need to spend 2*m - a full round for this small batch. 

But if n does not divide into k, there is some food left to cook 
after applying the previous formula, it is equal to n % k.
We can have a full round of 2*m minutes for this leftover batch, 
but it is not always needed. 

We can remove n % k pieces from the first batch 
when the first side is cooked and place them aside, 
then add the next pieces. 
In the end, there will remain another n%k pieces with one side cooked, 
and we can add this n % k pieces we put aside. 
Then we will cook it for only m minutes (since one side is already cooked) 
and will have all of the food cooked.
So we can just add m to the total time computed previously. 

But this method is not always possible. 
Of course, if 2*(n%k) > k, 
the last operation of the above described method would not be possible, 
so we would have to spend the full 2*m to cook that n%k in a usual way. 
"""

k = int(input())
m = int(input())
n = int(input())
full_time = n//k * 2*m
if n < k:
    full_time += 2*m
elif n % k != 0:
    full_time += m if 2*(n % k) <= k else 2*m
print(full_time)
