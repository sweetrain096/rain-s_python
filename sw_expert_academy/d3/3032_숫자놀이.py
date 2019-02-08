import sys
sys.stdin = open("3032_input.txt")

def GCD(a, b):
    bs = []
    while True :
        r = a % b
        if not r :
            return bs
        a = b
        b = r
        bs.append(b)




for tc in range(int(input())):
    a, b = map(int, input().split())
    x, y = 0, 0
    bs = GCD(a, b)


    for n in bs:
        y = (1 - a * n)/b
        if y == int(y):
            break

    if n == 0 or int(y) == 0 :
        print(f"#{tc + 1} -1")

    else:
        print(f"#{tc + 1} {n} {int(y)}")

