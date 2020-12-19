

with open("input.txt") as f:
    input = f.readlines()

valid = 0
for line in input:
    stuff, password = line.split(':')
    nums, letter = stuff.split(' ')
    count = password.count(letter)
    num_min, num_max = nums.split('-')
    num_min = int(num_min)
    num_max = int(num_max)
    if num_min <= count <= num_max:
        valid += 1

print(valid)





