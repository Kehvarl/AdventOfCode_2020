
with open("input.txt") as f:
    content = f.readlines()

groups = []

current = set()
for line in content:
    if line.strip() == '':
        groups.append(current)
        current = set()
    else:
        current.update(line.strip())

answers = [len(x) for x in groups]
print(groups)
print(answers)
print(sum(answers))


