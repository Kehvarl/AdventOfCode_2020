import collections

with open("test.txt") as f:
    content = f.readlines()

monster = ['                  # ',  # 18
           "#    ##    ##    ###",  # 0, 5, 6, 11, 12, 17, 18, 19
           "#  #  #  #  #  #    "]  # 0, 3, 6, 9, 12, 15

tiles = {}
tiles_edges = {}

tile_num = 0

for line in content:
    if line.startswith("Tile"):
        tile_num = int(line.strip().strip(":").split(" ")[1])
        tiles[tile_num] = []
        tiles_edges[tile_num] = ["", "", "", ""]
    elif line.strip() == '':
        continue
    else:
        tiles[tile_num].append(line.strip())

for tile in tiles:
    lines = tiles[tile]
    tiles_edges[tile] = [''.join(l[0] for l in lines)[::-1], lines[0], ''.join(l[-1] for l in lines), lines[-1][::-1]]


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


# def flip(flip_tile):
#     for line_index, tile_line in enumerate(flip_tile):
#         flip_tile[line_index] = tile_line[::-1]
#     return flip_tile
#
#
# def rotate(rotate_tile):
#     new_tile = ["" for _ in range(len(rotate_tile))]
#     for line_index, tile_line in enumerate(rotate_tile):
#         for c_index, char in enumerate(tile_line.split()):
#             new_tile[c_index] += char
#     return flip(new_tile)


def flip(lines):
    return[l[::-1] for l in lines]


def rotate(lines):
    s = []
    for row in range(len(lines)):
        s.append(''.join(l[-1-row] for l in lines))
    return s


def edges(lines):
    return [''.join(l[0] for l in lines)[::-1], lines[0], ''.join(l[-1] for l in lines), lines[-1][::-1]]


edgecount = collections.defaultdict(int)
edgetotile = collections.defaultdict(list)

for head, lines in tiles.items():
    ee = edges(lines)  # (left, top, right, bottom)
    for e in ee:
        e = min(e, e[::-1])
        edgecount[e] += 1
        edgetotile[e].append(head)


used = set()

assembly = [[]]


def go():
    p = 1
    for head, lines in tiles.items():

        if len(matches[head]) == 2:
            p *= head

            # for part 1, remove the following code:
            ll = lines
            for _ in range(4):
                e = edges(ll)
                if edgecount[min(e[0], e[0][::-1])] == 1 and edgecount[min(e[1], e[1][::-1])] == 1:
                    assembly[0].append(ll)
                    used.add(head)
                    return
                ll = flip(ll)
                if edgecount[min(e[0], e[0][::-1])] == 1 and edgecount[min(e[1], e[1][::-1])] == 1:
                    assembly[0].append(ll)
                    used.add(head)
                    return
                ll = flip(ll)
                ll = rotate(ll)
            assert False
go()

