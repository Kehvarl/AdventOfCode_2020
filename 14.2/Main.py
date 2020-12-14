
with open("input.txt") as f:
    content = f.readlines()

mask = ""
memory = {}


def set_value(val, set_mask):
    for i in range(len(set_mask)):
        if set_mask[i] == "1":
            val = val | (1 << (35 - i))

    return val


def get_addresses(mask, addr):
    addresses = [addr]
    for i in range(len(mask)):
        if mask[i] == "X":
            t_mask = mask[0:i] + "." + mask[i + 1:]
            addr |= (1 << (35 - i))
            addresses.extend(get_addresses(t_mask, addr))
            addr &= ~(1 << (35 - i))
            addresses.extend(get_addresses(t_mask, addr))
    return addresses


for line in content:
    command, value = line.strip().split(' = ')
    if command == "mask":
        mask = value
    else:
        value = int(value)
        addrresses = get_addresses(mask, set_value(int(command.strip("mem[").strip("]")), mask))
        for addr in addrresses:
            memory[addr] = value


print(memory)
print(sum(memory.values()))
