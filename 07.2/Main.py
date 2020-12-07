
with open("input.txt") as f:
    content = f.readlines()


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


def decode_bag(bag_color):
    if len(bag_rules[bag_color]) == 0:
        return 0

    total = 0
    for search_bag in bag_rules[bag_color]:
        bags = bag_rules[bag_color][search_bag]
        inside = decode_bag(search_bag)
        total += bags + bags * inside

    return total


print(decode_bag('shiny gold'))
