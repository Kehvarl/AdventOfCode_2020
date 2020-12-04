
with open("input.txt") as f:
    content = f.readlines()

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


ports = 0
fields = []
for line in content:
    if line.strip() == '':
        for f in req_fields:
            if f not in fields:
                break
        else:
            ports += 1

        current = []
        fields = []

    fields.extend([x.split(':')[0] for x in line.split()])


print(ports)
