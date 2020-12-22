
with open("input.txt") as f:
    content = f.read()

p1, p2 = content.split("\n\n")
p1 = p1.strip().split('\n')
p2 = p2.strip().split('\n')

player1 = [int(x) for x in p1[1:]]
player2 = [int(x) for x in p2[1:]]


def turn(pp1, pp2):
    if pp1 > pp2:
        return (pp1, pp2), ()
    else:
        return (), (pp2, pp1)


while len(player1) > 0 and len(player2) > 0:
    w1, w2 = turn(player1.pop(0), player2.pop(0))
    player1.extend(w1)
    player2.extend(w2)

winner = player1 if len(player1) > len(player2) else player2
total = 0
while len(winner) > 0:
    m = len(winner)
    total += m * winner.pop(0)

print(total)
