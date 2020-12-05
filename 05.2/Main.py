
with open("input.txt") as f:
    content = f.readlines()


def seat_decode(boarding_pass):
    row = boarding_pass[:7]
    col = boarding_pass[7::]

    row = int(row.replace("B", "1").replace("F", "0"), 2)
    col = int(col.replace("L", "0").replace("R", "1"), 2)

    return row, col, (row * 8 + col)


seats = [seat_decode(b)[2] for b in content]

seats.sort()

for s in range(len(seats)-1):
    if seats[s+1] > seats[s] + 1:
        print(seats[s] + 1)

print(max(seats))
