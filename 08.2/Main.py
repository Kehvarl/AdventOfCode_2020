
with open("input.txt") as f:
    content = f.readlines()


running = True
swap = 0
acc = 0

while running:
    acc = 0
    line = 0
    executed = set()
    while True:
        if line >= len(content):
            running = False
            print("swapped: ", swap)
            break
        if line in executed:
            swap += 1
            print(line)
            break
        operation, argument = content[line].strip().split(' ')

        if swap == line:
            if operation == "jmp":
                operation = "nop"
            elif operation == "nop":
                operation = "jmp"

        executed.add(line)
        print(line, operation, argument)

        if operation == "nop":
            line += 1
        elif operation == "acc":
            acc += int(argument)
            line += 1
        elif operation == "jmp":
            line += int(argument)


print(acc)
