
with open("input.txt") as f:
    content = [int(x) for x in f.readlines()]

current_joltage = 0
content.sort()
transitions = {1: 0, 2: 0, 3: 1}
for adapter in content:
    transitions[adapter - current_joltage] += 1
    current_joltage = adapter

print(transitions)
print(transitions[1] * transitions[3])
