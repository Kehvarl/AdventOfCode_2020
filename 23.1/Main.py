
data = [1, 3, 5, 4, 6, 8, 7, 2, 9]

test = [3, 8, 9, 1, 2, 5, 4, 6, 7]

cups = data[:]

for _ in range(100):
    current = cups[0]
    removed = cups[1:4]
    working_set = cups[4:]

    destination = current - 1
    while destination not in working_set:
        destination -= 1
        if destination < min(cups):
            destination = max(cups)

    index = working_set.index(destination)
    cups = working_set[:index + 1] + removed + working_set[index + 1:] + [current]

print(''.join([str(x) for x in cups[1:]]))




