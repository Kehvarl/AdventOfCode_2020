
with open("test.txt") as f:
    content = f.readlines()

neighbors = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]
neighbors.remove((0, 0, 0))

conway_cube = {}
for row, line in enumerate(content):
    for col, ch in enumerate(line):
        conway_cube[(row, col, 0, 0)] = ch


def turn(cube):
    temp_cube = {}
    for x in range(min(k[0] for k in cube.keys()) - 1, max(k[0] for k in cube.keys()) + 2):
        for y in range(min(k[1] for k in cube.keys()) - 1, max(k[1] for k in cube.keys()) + 2):
            for z in range(min(k[2] for k in cube.keys()) - 1, max(k[2] for k in cube.keys()) + 2):
                for q in range(min(k[3] for k in cube.keys()) - 1, max(k[3] for k in cube.keys()) + 2):
                    cell = cube.get((x, y, z, q), '.')
                    active = 0
                    for (cx, cy, cz) in neighbors:
                        for cq in (-1, 0, 1):
                            if cube.get((x+cx, y+cy, z+cz, q+cq), '.') == '#':
                                active += 1
                    if cell == '#':
                        if active in [2, 3]:
                            temp_cube[(x, y, z, q)] = '#'
                    elif cell == '.':
                        if active == 3:
                            temp_cube[(x, y, z, q)] = '#'
    return temp_cube


for t in range(6):
    conway_cube = turn(conway_cube)

total = 0
for x in range(min(k[0] for k in conway_cube.keys()), max(k[0] for k in conway_cube.keys()) + 1):
    for y in range(min(k[1] for k in conway_cube.keys()), max(k[1] for k in conway_cube.keys()) + 1):
        for z in range(min(k[2] for k in conway_cube.keys()), max(k[2] for k in conway_cube.keys()) + 1):
            for q in range(min(k[3] for k in conway_cube.keys()), max(k[3] for k in conway_cube.keys()) + 1):
                if conway_cube.get((x, y, z, q), '.') == '#':
                    total += 1

print(total)


