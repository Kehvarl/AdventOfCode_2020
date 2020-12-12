import math

with open("input.txt") as f:
    content = f.readlines()

facing = "E"
x = 0
y = 0
wx = 10
wy = -1


def move(move_direction, distance):
    move_x = 0
    move_y = 0
    if move_direction == "N":
        move_y -= distance
    elif move_direction == "S":
        move_y += distance
    elif move_direction == "E":
        move_x += distance
    elif move_direction == "W":
        move_x -= distance

    return move_x, move_y


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


def rotate_waypoint(cx, cy, rotate, amount):
    if rotate == "L":
        amount = -amount

    amount = math.radians(amount)
    tx = math.cos(amount) * cx - math.sin(amount) * cy
    ty = math.sin(amount) * cx + math.cos(amount) * cy
    tx = int(round(tx))
    ty = int(round(ty))

    return tx, ty


print(x, y, ':', wx, wy)
for line in content:
    direction = line[0]
    value = int(line[1:])

    if direction in ['L', 'R']:
        wx, wy = rotate_waypoint(wx, wy, direction, value)

    elif direction == "F":
        for i in range(value):
            x += wx
            y += wy
    else:
        nx, ny = move(direction, value)
        wx += nx
        wy += ny

    print(x, y, ':', wx, wy)

print(x, y, abs(x)+abs(y))
