import re
import operator

with open("input.txt") as f:
    content = f.readlines()


GROUP = re.compile(r'\(([^)(]+)\)')
ADD = re.compile(r'(\d+\s+\+\s+\d+)')
OPS = {'+': operator.add, '*': operator.mul}


def calc(expr, add=False):
    grouping = GROUP.findall(expr)
    while grouping:
        expr = GROUP.sub(calc(grouping[0], add=add), expr, 1)
        grouping = GROUP.findall(expr)
    if add:
        addition = ADD.findall(expr)
        while addition:
            expr = ADD.sub(calc(addition[0], add=False), expr, 1)
            addition = ADD.findall(expr)

    terms = expr.split()
    result = int(terms.pop(0))
    for _ in range(len(terms)//2):
        result = OPS[terms.pop(0)](result, int(terms.pop(0)))
    return str(result)


total = 0
for line in content:
    total += int(calc(line, add=True))
print(total)
