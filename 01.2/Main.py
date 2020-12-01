

with open("input.txt") as f:
    content = f.readlines()

content = [int(num.strip()) for num in content]

for v1 in content:
    for v2 in content:
        for v3 in content:
            if v1 + v2 + v3 == 2020:
                print(v1, v2, v3, (v1*v2*v3))
