
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

tiles = {}

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

print(tiles)

black = 0
for tile in tiles:
    if tiles[tile]:
        black += 1

print(black)
