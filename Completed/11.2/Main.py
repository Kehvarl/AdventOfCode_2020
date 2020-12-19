import copy

with open("input.txt") as f:
    content = f.readlines()

seat_map = []

for line in content:
    seat_map.append(list(line.strip()))

neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]


def first_occupied(row, col, rm, cm):
    iteration = 1
    while True:
        if (0 <= row + (rm * iteration) < len(seat_map)
                and 0 <= col + (cm * iteration) < len(seat_map[0])):
            if seat_map[row + (rm * iteration)][col + (cm * iteration)] == "#":
                return 1
            if seat_map[row + (rm * iteration)][col + (cm * iteration)] == "L":
                return 0
        else:
            return 0
        iteration += 1


changed = True
while changed:
    changed = False
    new_map = copy.deepcopy(seat_map)
    for row in range(len(seat_map)):
        for col in range(len(seat_map[0])):
            empty_neighbors = 0
            occupied = 0
            if seat_map[row][col] == ".":
                continue

            for rm, cm in neighbors:
                occupied += first_occupied(row, col, rm, cm)

            if seat_map[row][col] == "L" and occupied == 0:
                new_map[row][col] = "#"
                changed = True
            elif seat_map[row][col] == "#" and occupied >= 5:
                new_map[row][col] = "L"
                changed = True
    seat_map = copy.deepcopy(new_map)

    # for line in seat_map:
    #    print(''.join(line))
    # print()
    # pass

occupied = 0
for line in seat_map:
    for seat in line:
        if seat == "#":
            occupied += 1
print(occupied)
