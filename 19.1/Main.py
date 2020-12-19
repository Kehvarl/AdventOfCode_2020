
with open("test.txt") as f:
    content = f.readlines()

rules = {}
lines = []
for line in content:
    if ':' in line:
        rule, requirements = line.strip().split(": ")
        requirements = [x.strip().strip('"') for x in requirements.split("|")]
        rules[int(rule)] = requirements
    else:
        lines.append(line)

for index in rules:
    r = []
    for rule in rules[index]:
        if rule[0].isnumeric():
            r.append([int(x) for x in rule.split(" ")])
        else:
            r = rule
    rules[index] = r


def rule_solver(rule):
    if type(rule) == str:
        return rule
    if type(rule) == int:
        return rule_solver(rules[rule])

    a, b = rule
    a = rule_solver(a)
    b = rule_solver(b)
    return [a, b]


goal = rules[0][:]
print(rules)
print(goal[0])
s = rule_solver(goal[0])
solutions = set()
