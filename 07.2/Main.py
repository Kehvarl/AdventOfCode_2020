
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


def decode_bag(color):
    if len(bag_rules[color]) == 0:
        return 0

    print(bag_rules[color])
    total = 0
    for bag in bag_rules[color]:
        bags = bag_rules[color][bag]
        inside = decode_bag(bag)
        total += bags + bags * inside

    return total


print(decode_bag('shiny gold'))
# print(decode_bag('dark olive'))
