import copy

with open("input.txt") as f:
    content = f.readlines()

seat_map = []

for line in content:
    seat_map.append(list(line.strip()))

neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]

for line in seat_map:
    print(''.join(line))


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
                if (0 <= row + rm < len(seat_map)
                        and 0 <= col + cm < len(seat_map[0])):
                    if seat_map[row + rm][col + cm] == "L":
                        empty_neighbors += 1
                    if seat_map[row + rm][col + cm] == "#":
                        occupied += 1

            if seat_map[row][col] == "L" and occupied == 0:
                new_map[row][col] = "#"
                changed = True
            elif seat_map[row][col] == "#" and occupied >= 4:
                new_map[row][col] = "L"
                changed = True
    seat_map = copy.deepcopy(new_map)

occupied = 0
for line in seat_map:
    for seat in line:
        if seat == "#":
            occupied += 1
print(occupied)
