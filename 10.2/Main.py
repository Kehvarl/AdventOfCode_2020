
with open("input.txt") as f:
    content = [int(x) for x in f.readlines()]

content.append(max(content) + 3)
content.sort()


memo = {0: 1}

for v in content:
    memo[v] = 0
    for n in [1, 2, 3]:
        if v - n in memo:
            memo[v] += memo[v - n]

print(memo[max(content)])
print(memo)
