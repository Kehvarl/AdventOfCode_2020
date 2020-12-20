
with open("test.txt") as f:
    content = f.readlines()

monster = ['                  # ',  # 18
           "#    ##    ##    ###",  # 0, 5, 6, 11, 12, 17, 18, 19
           "#  #  #  #  #  #    "]  # 0, 3, 6, 9, 12, 15

tiles = {}
tiles_edges = {}

tile_num = 0
t_line = 0

for line in content:
    if line.startswith("Tile"):
        tile_num = int(line.strip().strip(":").split(" ")[1])
        t_line = 0
        tiles[tile_num] = []
        tiles_edges[tile_num] = ["", "", "", ""]
    elif line.strip() == '':
        continue
    else:
        tiles[tile_num].append(line.strip())
        if t_line == 0:
            tiles_edges[tile_num][0] = line.strip()
        if t_line == 9:
            tiles_edges[tile_num][1] = line.strip()
            tiles_edges[tile_num][2] += line.strip()[0]
            tiles_edges[tile_num][3] += line.strip()[-1]
        else:
            tiles_edges[tile_num][2] += line.strip()[0]
            tiles_edges[tile_num][3] += line.strip()[-1]
        t_line += 1


def match_tile(tile_a, tile_b):
    t_edges_a = tiles_edges[tile_a]
    t_edges_b = tiles_edges[tile_b]
    for edge in t_edges_a:
        if edge in t_edges_b:
            return True, t_edges_a.index(edge), t_edges_b.index(edge), False
        elif edge[::-1] in t_edges_b:
            return True, t_edges_a.index(edge), t_edges_b.index(edge[::-1]), True
    return False, -1, -1, False


matches = {}
for tile_id, tile in tiles.items():
    for tile2_id, tile2 in tiles.items():
        if tile2_id == tile_id:
            continue
        match, side_a, side_b, rev = match_tile(tile_id, tile2_id)
        if match:
            if tile_id not in matches:
                matches[tile_id] = set()
            matches[tile_id].add((tile2_id, side_a, side_b, rev))

for tile_id, tile in tiles.items():
    tile = tile[1:-1]
    for index, line in enumerate(tile):
        tile[index] = line[1:-1]


def flip(flip_tile):
    for line_index, tile_line in enumerate(flip_tile):
        flip_tile[line_index] = tile_line[::-1]


def rotate(rotate_tile):
    new_tile = ["" for _ in range(len(tile))]
    for line_index, tile_line in rotate_tile:
        for c_index, char in enumerate(tile_line.split()):
            new_tile[c_index] += char
    return new_tile


image = []
for k, m in matches.items():
    pass
