with open("input.txt") as f:
    data = [int(x) for x in f.readlines()]

nums = [v for v in data if (2020 - v) in data]

print(nums[0], nums[1], nums[0]*nums[1])
