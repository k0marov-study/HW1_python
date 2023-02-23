TO_THE_RIGHT = "RIGHT"
TO_THE_LEFT = "LEFT"


k = int(input())
n = int(input())
petya_row = int(input())  # starting from 1
petya_place_name = input()  # one of the TO_THE_RIGHT or TO_THE_LEFT constants
petya_place = 0 if petya_place_name == TO_THE_RIGHT else 1

petya_position = 2*(petya_row-1) + 1 + petya_place

row_count = (n+1) // 2

best_row = 0
best_place_name = ""

for pos in (petya_position - k, petya_position + k):
    row = (pos+1) // 2
    place = 1 - pos % 2

    alone_and_left = row == row_count and n % 2 and place == 1
    pos_valid = 1 <= row <= row_count and not alone_and_left
    diff = abs(petya_row - row)
    best_diff = abs(petya_row - best_row)
    if pos_valid and (not best_row or diff <= best_diff):
        best_row = row
        best_place_name = TO_THE_RIGHT if place == 0 else TO_THE_LEFT

if best_row:
    print(best_row, best_place_name)
else:
    print(-1)
