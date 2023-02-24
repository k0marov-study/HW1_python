PLACE_RIGHT = "RIGHT"
PLACE_LEFT = "LEFT"
n = int(input())
k = int(input())
petya_row = int(input())  # starting from 1
petya_place = PLACE_RIGHT if int(input()) == 1 else PLACE_LEFT

petya_position = 2*(petya_row-1) + 1 + (0 if petya_place == PLACE_RIGHT else 1)

row_count = (n+1) // 2

best_row = None
best_place = None

for pos in (petya_position - k, petya_position + k):
    row = (pos+1) // 2
    place = PLACE_RIGHT if pos % 2 else PLACE_LEFT

    alone_and_left = row == row_count and n % 2 and place == PLACE_LEFT
    pos_valid = 1 <= row <= row_count and not alone_and_left

    diff = abs(petya_row - row)
    pos_better = best_row is None or diff <= abs(petya_row - best_row)
    if pos_valid and pos_better:
        best_row = row
        best_place = place

if best_row is None:
    print(-1)
else:
    print(best_row, 1 if best_place == PLACE_RIGHT else 2)
