
with open("input.txt") as f:
    content = f.read()

p1, p2 = content.split("\n\n")
p1 = p1.strip().split('\n')
p2 = p2.strip().split('\n')

player1 = [int(x) for x in p1[1:]]
player2 = [int(x) for x in p2[1:]]


def game(deck1, deck2):
    rounds = set()
    while len(deck1) > 0 and len(deck2) > 0:
        if tuple(deck1)in rounds and tuple(deck2) in rounds:
            return deck1, deck1, deck2
        rounds.add(tuple(deck1))
        rounds.add(tuple(deck2))

        pc1 = deck1.pop(0)
        pc2 = deck2.pop(0)

        if pc1 <= len(deck1) and pc2 <= len(deck2):
            win, pd1, pd2 = game(deck1[0:pc1], deck2[0:pc2])
            if win == pd1:
                deck1.extend((pc1, pc2))
            else:
                deck2.extend((pc2, pc1))
        else:
            if pc1 > pc2:
                deck1.extend((pc1, pc2))
            else:
                deck2.extend((pc2, pc1))

    return deck1 if len(deck1) > len(deck2) else deck2, deck1, deck2


w, d1, d2 = game(player1, player2)

print(d1)
total = 0
while len(d1) > 0:
    m = len(d1)
    total += m * d1.pop(0)
print(total)


print(d2)
total = 0
while len(d2) > 0:
    m = len(d2)
    total += m * d2.pop(0)
print(total)
