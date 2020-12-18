
with open("input.txt") as f:
    content = f.readlines()


def operate(accumulator, operator, operand):
    operand = int(operand)
    if operator is None:
        accumulator = operand
    elif operator == '+':
        accumulator += operand
    elif operator == '-':
        accumulator -= operand
    elif operator == '*':
        accumulator *= operand
    elif operator == '/':
        accumulator /= operand
    return accumulator

def parse_line(line):
    accum = 0
    operation = None
    i = 0

    while i < len(line):
        char = line[i]
        if char == "(":
            a, ti = parse_line(line[i+1:])
            accum = operate(accum, operation, a)
            i = i + ti
        elif char == ")":
            return accum, i+1
        elif char in ['+', '-', '*', '/']:
            operation = char
        elif char.isnumeric():
            accum = operate(accum, operation, int(char))

        i += 1

    return accum, i


total = 0
for line in content:
    a, i = parse_line(line)
    total += a
print(total)