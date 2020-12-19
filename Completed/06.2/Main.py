
with open("input.txt") as f:
    content = f.readlines()

groups = []
default = set()
default.update('abcdefghijklmnopqrstuvwxyz')
current = default

for line in content:
    if line.strip() == '':
        groups.append(current)
        current = default
    else:
        current = current.intersection(line.strip())

print(sum([len(x) for x in groups]))
