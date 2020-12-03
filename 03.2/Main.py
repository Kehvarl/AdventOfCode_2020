
with open("input.txt") as f:
    data_in = f.readlines()


def is_impact(x, y):
    return data_in[y][x]


def check_slope(r, d):
    y = 0
    x = 0
    tree = 0

    while y < len(data_in):
        if is_impact(x, y) == '#':
            tree += 1
        x = (x + r) % (len(data_in[0]) - 1)
        y += d

    return tree

tests = []
tests.append(check_slope(1, 1))
tests.append(check_slope(3, 1))
tests.append(check_slope(5, 1))
tests.append(check_slope(7, 1))
tests.append(check_slope(1, 2))

print(tests)
print(tests[0] * tests[1] * tests[2] * tests[3] * tests[4])

