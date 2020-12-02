

with open("input.txt") as f:
    data_in = f.readlines()

valid = 0
for line in data_in:
    stuff, password = line.split(':')
    nums, letter = stuff.split(' ')
    num_min, num_max = nums.split('-')
    num_min = int(num_min)
    num_max = int(num_max)
    password = password.strip()
    pos1 = password[num_min - 1] == letter
    pos2 = password[num_max - 1] == letter

    if pos2 ^ pos1:
        valid += 1


print(valid)
