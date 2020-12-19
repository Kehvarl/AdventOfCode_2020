
with open("input.txt") as f:
    content = [int(x) for x in f.readlines()]


preamble = 25
target = 400480901

for start in range(len(content)):
    for end in range(1, len(content)):
        if sum(content[start:end]) == target:
            print(min(content[start:end]), max(content[start:end]), min(content[start:end]) + max(content[start:end]))
        elif sum(content[start:end]) > target:
            break
