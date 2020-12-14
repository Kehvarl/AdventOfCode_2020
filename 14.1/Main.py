
with open("input.txt") as f:
    content = f.readlines()

mask = ""
memory = {}


def set_value(val, set_mask):
    for i in range(len(set_mask)):
        if set_mask[i] == "1":
            val = val | (1 << (35 - i))
        elif set_mask[i] == "0":
            val = val & ~(1 << (35 - i))
    return val


for line in content:
    command, value = line.strip().split(' = ')
    if command == "mask":
        mask = value
    else:
        value = set_value(int(value), mask)
        addr = int(command.strip("mem[").strip("]"))
        memory[addr] = value


print(memory, sum(memory.values()))
