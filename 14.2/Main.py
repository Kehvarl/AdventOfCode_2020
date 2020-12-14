
with open("input.txt") as f:
    content = f.readlines()

mask = ""
memory = {}


def get_masks(index, working_mask):
    if not working_mask:
        yield 0
    else:
        for m in get_masks(index // 2, working_mask[:-1]):
            if working_mask[-1] == '0':
                yield 2 * m + index % 2
            if working_mask[-1] == '1':
                yield 2 * m + 1
            if working_mask[-1] == 'X':
                yield 2 * m + 0
                yield 2 * m + 1


for line in content:
    command, value = line.strip().split(' = ')
    if command == "mask":
        mask = value
    else:
        value = int(value)
        addr = int(command.strip("mem[").strip("]"))
        for mask_addr in get_masks(addr, mask):
            memory[mask_addr] = value


print(memory)
print(sum(memory.values()))
