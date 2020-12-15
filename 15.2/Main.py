
with open("input.txt") as f:
    content = [int(x) for x in f.readline().split(',')]

content.reverse()
nums = {}
last = None

for turn in range(30000000):
    if content:
        last = content.pop()
    else:
        if len(nums[last]) == 1:
            last = 0
        else:
            last = nums[last][-1] - nums[last][-2]

    if last not in nums:
        nums[last] = [turn]
    else:
        nums[last].append(turn)

print(last)
