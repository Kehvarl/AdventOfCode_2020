
with open("input.txt") as f:
    content = [int(x) for x in f.readlines()]

current_joltage = 0
content.sort()
transitions = {1: 0, 2: 0, 3: 0}
for adapter in content:
    if adapter > current_joltage + 3:
        print("Broken Chain: ", current_joltage, adapter)
        break
    transitions[adapter - current_joltage] += 1
    current_joltage = adapter

transitions[3] += 1

print(transitions)
print(transitions[1] * transitions[3])