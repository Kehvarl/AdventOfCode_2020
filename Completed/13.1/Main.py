
with open("input.txt") as f:
    timestamp = int(f.readline())
    bus_ids = [int(x) for x in f.readline().split(',') if x.isnumeric()]


min_bus = 99
bus_delta = 1

print(bus_ids)

for id in bus_ids:
    if ((timestamp // id) +1) - (timestamp / id) < bus_delta:
        bus_delta = ((timestamp // id) + 1) - (timestamp / id)
        min_bus = id
    print(id, timestamp // id, timestamp / id)


diff = 1
print(timestamp)
print(min_bus, timestamp // min_bus, timestamp / min_bus)
while (timestamp + diff) % min_bus != 0:
    diff += 1
print(diff, min_bus, diff * min_bus)
print(timestamp + diff, (timestamp + diff) / min_bus)


