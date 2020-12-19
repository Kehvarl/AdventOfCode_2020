

with open("input.txt") as f:
    data_in = f.readlines()


def is_impact(x, y):
    return data_in[y][x]

y = 0
x = 0
tree = 0

while y < len(data_in):
    if is_impact(x, y) == '#':
        tree += 1
    x = (x + 3) % (len(data_in[0]) -1)
    y += 1

print(tree)
