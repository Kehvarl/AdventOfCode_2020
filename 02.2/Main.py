import re

with open("input.txt") as f:
    data_in = f.readlines()

valid = 0
for line in data_in:
    pos1, pos2, letter, skip, password = re.split('[: \-]', line)
    if (password[int(pos1) - 1] == letter) ^ (password[int(pos2) - 1] == letter):
        valid += 1


print(valid)
