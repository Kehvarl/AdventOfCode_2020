from functools import reduce

with open("input.txt") as f:
    ignore = f.readline()
    bus_ids = [x for x in f.readline().strip().split(',')]


def chinese_remainder(cr_n, cr_a):
    """
    From Rosetta Code
    https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    """
    cr_sum = 0
    prod = reduce(lambda a, b: a * b, cr_n)
    for n_i, a_i in zip(cr_n, cr_a):
        p = prod // n_i
        cr_sum += a_i * mul_inv(p, n_i) * p
    return cr_sum % prod


def mul_inv(mi_a, mi_b):
    """
    From Rosetta Code
    https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    """
    b0 = mi_b
    x0, x1 = 0, 1
    if mi_b == 1:
        return 1
    while mi_a > 1:
        q = mi_a // mi_b
        mi_a, mi_b = mi_b, mi_a % mi_b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


bus = []
interval = []

for i in range(len(bus_ids)):
    if bus_ids[i].isnumeric():
        temp_bus = int(bus_ids[i])
        bus_ids[i] = temp_bus
        bus.append(temp_bus)
        interval.append((temp_bus - i) % temp_bus)

print(chinese_remainder(bus, interval))


# Alternate solution.
from itertools import count
n = int(ignore)
buses = tuple((i, b) for i, b in enumerate(bus_ids) if isinstance(b, int))
step = 1
print(buses)
for i, b in buses:
    n = next(c for c in count(n, step) if (c + i) % b == 0)
    step *= b
print(n)
