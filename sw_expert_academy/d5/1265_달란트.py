import sys
sys.stdin = open("1265_input.txt")

for tc in range(int(input())):
    num, p = map(int, input().split())
    k = num // p
    r = num % p
    if r:
        k += 1
    else:
        r = -1
    calc = num
    result = 1
    for i in range(p):
        if r > 0:
            r -= 1
        elif not r:
            k -= 1
            r = -1
        calc -= k
        result *= k

        # print(k, r, result, calc)




    print(f"#{tc + 1} {result}")
