import random

a = [0 for _ in range(46)]
cnt = 0
while cnt < 6:
    num = random.randrange(1, 46)
    if not a[num]:
        print(num)
        a[num] = 1
        cnt += 1
