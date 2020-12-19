
with open("input.txt") as f:
    content = f.readlines()


desired_bag = set()
desired_bag.add('shiny gold')
bag_rules = {}

for rule in content:
    bag, contains = rule.split('contain')
    bag = bag.strip().replace(' bags', '')
    if bag not in bag_rules:
        bag_rules[bag] = {}

    for allowed in contains.split(','):
        if allowed.strip()[:2] != "no":
            number = allowed[1]
            color = allowed[2::].strip().replace('.', '').replace(' bags', '').replace(' bag', '')
            if color not in bag_rules[bag]:
                bag_rules[bag][color] = 0
            bag_rules[bag][color] += int(number)

for x in range(50):
    for rule in bag_rules:
        for bag in bag_rules[rule]:
            if bag in desired_bag:
                desired_bag.add(rule)

print(desired_bag)
print(len(desired_bag))

