
with open("input.txt") as f:
    content = f.readlines()

tiles = {}
tiles_edges = {}

tile_num = 0
tline=0
for line in content:
    if line.startswith("Tile"):
        tile_num = int(line.strip().strip(":").split(" ")[1])
        tline=0
        tiles[tile_num] = []
        tiles_edges[tile_num] = ["", "", "", ""]
    elif line.strip() == '':
        continue
    else:
        tiles[tile_num].append(line.strip())
        if tline == 0:
            tiles_edges[tile_num][0] = line.strip()
        if tline == 9:
            tiles_edges[tile_num][1] = line.strip()
            tiles_edges[tile_num][2] += line.strip()[0]
            tiles_edges[tile_num][3] += line.strip()[-1]
        else:
            tiles_edges[tile_num][2] += line.strip()[0]
            tiles_edges[tile_num][3] += line.strip()[-1]
        tline += 1


def match_tile(tilea, tileb):
    t_edges_a = tiles_edges[tilea]
    t_edges_b = tiles_edges[tileb]
    for edge in t_edges_a:
        if edge in t_edges_b or edge[::-1] in t_edges_b:
            return True
    return False


matches = {}
for tile_id, tile in tiles.items():
    for tile2_id, tile2 in tiles.items():
        if tile2_id == tile_id:
            continue
        if match_tile(tile_id, tile2_id):
            if tile_id not in matches:
                matches[tile_id] = set()
            matches[tile_id].add(tile2_id)

print(matches)
total = 1
for k, m in matches.items():
    if len(m) == 2:
        print(k)
        total *= k
print(total)

