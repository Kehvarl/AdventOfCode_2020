
with open("input.txt") as f:
    content = f.readlines()


acc = 0
running = True
line = 0
executed = set()
while running:
    if line >= len(content) or line in executed:
        break
    operation, argument = content[line].strip().split(' ')
    executed.add(line)

    if operation == "nop":
        line += 1
    elif operation == "acc":
        acc += int(argument)
        line += 1
    elif operation == "jmp":
        line += int(argument)

print(acc)