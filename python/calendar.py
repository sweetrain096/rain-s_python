import sys
sys.stdin = open("calendar_input.txt")
def GCD(a, b) :
    while True :
        r = a % b
        if not r :
            return b
        a = b
        b = r

t = int(input())

for test_case in range(t):
    m, n, x, y = list(map(int, input().split()))
    gcd = GCD(n, m)
    print(m, n, x, y, gcd)
    result = -1

    cnt = int(n / GCD(n, m))
    print("cnt", cnt)
    first = x

    for month in range(cnt):
        if first == y :
            break
        first -= gcd
        if first <= 0:
            first += n
    result = (month) * m + x
    if month + 1 == cnt and first != y:
        result = -1



    print(result)
