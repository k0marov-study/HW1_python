def solve(n, k, petya_row, petya_place):
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
        return "-1"
    else:
        return f"{best_row} {best_place}"


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    petya_row = int(input())
    petya_place = int(input())
    print(solve(n, k, petya_row, petya_place))
