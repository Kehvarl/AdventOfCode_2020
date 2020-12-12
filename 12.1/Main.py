
with open("input.txt") as f:
    content = f.readlines()

facing = "E"
x = 0
y = 0


def move(move_direction, distance):
    x = 0
    y = 0
    if move_direction == "N":
        y -= distance
    elif move_direction == "S":
        y += distance
    elif move_direction == "E":
        x -= distance
    elif move_direction == "W":
        x += distance

    return x, y


def turn(current, rotate, amount):
    directions = ['N', 'E', 'S', 'W']
    current = directions.index(current)
    while amount > 0:
        if rotate == "R":
            current = (current + 1) % len(directions)
        elif rotate == "L":
            current = (current - 1) % len(directions)
        amount -= 90
    return directions[current]


for line in content:
    direction = line[0]
    value = int(line[1:])

    if direction == "L":
        facing= turn(facing, "L", value)
    elif direction == "R":
        facing = turn(facing, "R", value)
    elif direction == "F":
        nx, ny = move(facing, value)
        x += nx
        y += ny
    else:
        nx, ny = move(direction, value)
        x += nx
        y += ny


print(x, y, abs(x)+abs(y))