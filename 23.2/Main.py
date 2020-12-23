from collections import deque, defaultdict

data = [1, 3, 5, 4, 6, 8, 7, 2, 9]

test = [3, 8, 9, 1, 2, 5, 4, 6, 7]

cups = data[:] + list(range(max(data)+1, 1000001))

input = cups
current = input[0]
ring = {}
for i in range(len(input)):
    if i == len(input) - 1:
        ring[input[i]] = input[0]
    else:
        ring[input[i]] = input[i+1]


def round(ring,current):
    maximum = 1000000
    minimum = 1
    next = ring[current]
    outside = [None,None,None]
    for x in range(3):
        outside[x] = next
        next = ring[next]
    ring[current] = next
    dest = current - 1
    if dest == 0:
        dest = maximum
    while dest in outside:
        if dest > minimum:
            dest = dest - 1
        else:
            dest = maximum
    stitch = ring[dest]
    ring[dest] = outside[0]
    ring[outside[2]] = stitch
    return ring, next


for x in range(10000000):
    ring,current = round(ring,current)

print(ring[1]*ring[ring[1]])