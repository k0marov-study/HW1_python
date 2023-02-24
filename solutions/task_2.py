"""
If two points lie in the same quarter, 
the signs of their respective x and y coordinates 
must be equal.
"""

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

same_quarter = (x1 > 0) == (x2 > 0) and (y1 > 0) == (y2 > 0)

print("YES" if same_quarter else "NO")
