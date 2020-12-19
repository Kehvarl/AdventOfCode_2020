import re

with open("input.txt") as f:
    content = f.readlines()

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


ports = []
fields = []
current = []
for line in content:
    if line.strip() == '':
        for f in req_fields:
            if f not in fields:
                break
        else:
            ports.append(current)

        current = []
        fields = []

    current.extend([x for x in line.split()])
    fields.extend([x.split(':')[0] for x in line.split()])


valid_ports = 0
for port in ports:
    keys = [x.split(':')[0] for x in port]
    vals = [x.split(':')[1] for x in port]

    for x in range(len(keys)):
        key = keys[x]
        val = vals[x]
        if key == 'byr':
            if not (len(val) == 4 and 1910 <= int(val) <= 2002):
                break
        elif key == 'iyr':
            if not (len(val) == 4 and 2010 <= int(val) <= 2020):
                break
        elif key == 'eyr':
            if not (len(val) == 4 and 2020 <= int(val) <= 2030):
                break
        elif key == 'hgt':
            h = val[:-2]
            u = val[-2::]
            if u == 'cm':
                if not (150 <= int(h) <= 193):
                    break
            elif u == 'in':
                if not (59 <= int(h) <= 76):
                    break
            else:
                break

        elif key == 'hcl':
            if not re.match(r'#[0-9a-f]{6}', val):
                break
        elif key == 'ecl':
            if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                break
        elif key == 'pid':
            if len(val) != 9:
                break
    else:
        valid_ports += 1


print(valid_ports)
