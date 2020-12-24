from collections import defaultdict

with open("input.txt") as f:
    content = f.readlines()

directions = {
    'e': (1, 0),
    'se': (0.5, 1),
    'sw': (-0.5, 1),
    'w': (-1, 0),
    'nw': (-0.5, -1),
    'ne': (0.5, -1)
}

tiles = defaultdict(bool)

for line in content:
    line = line.strip()
    x, y = 0, 0
    while len(line) > 0:
        char = line[0]
        line = line[1:]
        if char in ['n', 's']:
            char += line[0]
            line = line[1:]
        dx, dy = directions[char]

        x += dx
        y += dy

    if (x, y) not in tiles:
        tiles[(x, y)] = True
    else:
        tiles[(x, y)] = not(tiles[x, y])
        for d in directions.values():
            if (x + d[0], y + d[1]) not in tiles:
                tiles[(x + d[0], y + d[1])] = False


for _ in range(100):
    temp_tiles = defaultdict(lambda: False)

    neighbors = defaultdict(lambda: 0)

    for (tx, ty), t_val in tiles.items():
        if t_val:
            for d in directions.values():
                neighbors[tx + d[0], ty + d[1]] += 1

    check = set(neighbors.keys()).union(set(tiles.keys()))
    for tile in check:
        if tiles[tile]:
            temp_tiles[tile] = not(neighbors[tile] not in [1, 2])
        else:
            if neighbors[tile] == 2:
                temp_tiles[tile] = True

    tiles = temp_tiles

black = 0
for tile in tiles:
    if tiles[tile]:
        black += 1

print(black)
