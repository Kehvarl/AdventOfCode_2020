

with open("input.txt") as f:
    content = f.readlines()


def seat_decode(boarding_pass):
    row = boarding_pass[:7]
    col = boarding_pass[7::]

    row = row.replace("B", "1")
    row = row.replace("F", "0")
    row = int(row, 2)

    col = col.replace("L", "0")
    col = col.replace("R", "1")
    col = int(col, 2)

    return row, col, (row * 8 + col)


seats = []
for boarding in content:
    seat = seat_decode(boarding)
    seats.append(seat[2])

seats.sort()

for s in range(len(seats)-1):
    if seats[s+1] > seats[s] + 1:
        print(seats[s] + 1)

print(max(seats))

