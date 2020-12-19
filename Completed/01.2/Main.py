from itertools import combinations

with open("input.txt") as f:
    content = f.readlines()

content = [int(num.strip()) for num in content]

for v1, v2, v3 in combinations(content, 3):
    if v1 + v2 + v3 == 2020:
        print(v1, v2, v3, (v1 * v2 * v3))
