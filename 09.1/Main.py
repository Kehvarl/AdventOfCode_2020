
with open("input.txt") as f:
    content = [int(x) for x in f.readlines()]


preamble = 25

for current in range(25, len(content)):
    cval = content[current]
    window = content[current - 25:current]
    for previous in range(25):
        pval = content[current - previous]
        if (cval - pval) in window:
            break
    else:
        print(cval)

