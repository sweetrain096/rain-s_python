import sys
sys.stdin = open("3032_input.txt")

def GCD(a, b):
    bs = []
    while True :
        r = a % b
        # print("r",r, "b", b)
        if not r :
            return bs
        a = b
        b = r
        bs.append(b)




for tc in range(int(input())):
    a, b = map(int, input().split())
    x = 0
    bs = GCD(a, b)

    print(bs)






    while True:

        y = (1 - a * x)/b

        if y == int(y):
            break

        y = (1 - a * (-x)) / b

        if type(y) == int:
            break
        x += 1

    print(f"#{tc + 1} {x} {int(y)}")

