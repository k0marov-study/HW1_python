"""
Let's say that a student's "position" is
his index (starting from 1) in the order in which the teacher gives variants.

It means that students with position 1, k + 1, 2*k + 1, ... will have variant 1.
2, k + 2, 2*k + 2, ... will have variant 2 and so on.

Then if Petya has position = x,
students with the same variant will have a position
of x + n*k, such that n lies in Z (all of the integer values).

So the closest students will have a position of x - k and x + k.

Lets now get their row and place from the position and check if they are valid
(also considering the requirement
that a student sitting alone must sit on the 1-st place),
then compare the distance to the Petya's row,
giving preference to x + k, since it is the student that sits behind Petya,
by evaluating it last.

In the end, we will have best_row and best_place
of the valid and closest position to Petya. Print it as the answer.

If best_row remained unset, then there is no valid rows, print "-1".
"""


n = int(input())
k = int(input())
petya_row = int(input())
petya_place = int(input())

petya_position = 2*(petya_row-1) + petya_place

row_count = (n+1) // 2

best_row = None
best_place = None

for pos in (petya_position - k, petya_position + k):
    row = (pos+1) // 2
    place = 1 if pos % 2 else 2

    alone_and_left = row == row_count and n % 2 and place == 2
    pos_valid = 1 <= row <= row_count and not alone_and_left

    diff = abs(petya_row - row)
    pos_better = best_row is None or diff <= abs(petya_row - best_row)
    if pos_valid and pos_better:
        best_row = row
        best_place = place

if best_row is None:
    print("-1")
else:
    print(best_row, best_place)
