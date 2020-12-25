
keys = [17115212, 3667832]
# keys = [5764801, 17807724]

start = 1
subject = 7
loop = 0
while True:
    start = (subject * start) % 20201227
    if start in keys:
        subject = [k for k in keys if k != start][0]
        break
    loop += 1

start = 1
for i in range(loop+1):
    start = (subject * start) % 20201227
print(subject, start)