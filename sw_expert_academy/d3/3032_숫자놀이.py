import sys
sys.stdin = open("3032_input.txt")

def GCD(a, b):
    bs = []
    while True :
        r = a % b
        bs.append(b)
        if not r :
            return bs
        a = b
        b = r


for tc in range(int(input())):
    a, b = map(int, input().split())
    x, y = 0.5, 0.5
    bs = GCD(a, b)

    for n in bs:
        y = (1 - a * n)/b
        if y == int(y):
            break

    if n == 0.5 and y == 0.5 :
        print(f"#{tc + 1} -1")

    else:
        print(f"#{tc + 1} {n} {int(y)}")

