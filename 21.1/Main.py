
with open("input.txt") as f:
    content = f.readlines()


allergens = {}
non_allergens = []

for line in content:
    a = line.index('(')
    ingredients = line[0:a].strip().split(" ")
    a = [x.strip() for x in line[a:-1][10:-1].split(", ")]

    non_allergens.extend(ingredients)

    for allergen in a:
        if allergen not in allergens:
            allergens[allergen] = set()
            allergens[allergen].update(ingredients)
        else:
            allergens[allergen] = allergens[allergen].intersection(ingredients)

working = True
while working:
    working = False
    for allergen in allergens:
        if len(allergens[allergen]) == 1:
            for e in allergens[allergen]:
                for allergen2 in allergens:
                    if allergen2 == allergen:
                        continue
                    if e in allergens[allergen2]:
                        allergens[allergen2].remove(e)
        else:
            working = True


for allergen in allergens:
    for e in allergens[allergen]:
        non_allergens = [n for n in non_allergens if n != e]


print(non_allergens)
print(len(non_allergens))