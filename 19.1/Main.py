
with open("input.txt") as f:
    content = f.read()

data_rules, data_messages = content.split('\n\n')
data_rules = data_rules.split('\n')
data_messages = data_messages.split('\n')

rules = {}

for line in data_rules:
    rule, requirements = line.strip().split(": ")
    requirements = [x.strip().strip('"') for x in requirements.split("|")]
    rules[int(rule)] = requirements

for index in rules:
    r = []
    for rule in rules.get(index, False):
        if rule[0].isnumeric():
            r.append([int(x) for x in rule.split(" ")])
        else:
            r = rule
    rules[index] = r

print(rules)


def match_rules(rule_nums, message):
    if not rule_nums:
        return not message
    rule_num, *rule_nums = rule_nums
    rule_match = rules[rule_num]
    if isinstance(rule_match, str):
        return (message.startswith(rule_match) and
                match_rules(rule_nums, message[len(rule_match):]))
    else:
        return any(match_rules(option + rule_nums, message)
                   for option in rule_match)


print(sum(match_rules([0], message) for message in data_messages))
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print(sum(match_rules([0], message) for message in data_messages))
