
with open("input.txt") as f:
    content = f.readlines()


rules = []
my_ticket = []
tickets = []

state = 0 # rules
for line in content:
    if line.strip() == '':
        state += 1
    else:
        if state == 0:
            rule, values = line.strip().split(':')
            a, b = values.split(' or ')
            loa, hia = a.split('-')
            lob, hib = b.split('-')
            r = list(range(int(loa), int(hia)+1))
            r.extend(list(range(int(lob), int(hib)+1)))
            rules.append((rule, r))
        if state == 1:
            if not line.startswith("your ticket"):
                my_ticket.extend([int(x) for x in line.split(',')])
        if state == 2:
            if not line.startswith("nearby ticket"):
                tickets.append([int(x) for x in line.split(',')])

invalid = []

for ticket in tickets:
    for x in ticket:
        x = int(x)
        valid = False
        for rule in rules:
            r, r_range = rule
            if x in r_range:
                valid = True
        if not valid:
            invalid.append(x)



print(rules)
print(my_ticket)
print(tickets)

print(invalid)
print(sum(invalid))