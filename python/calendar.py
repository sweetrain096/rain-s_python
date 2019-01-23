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
    lcm = int(n * m / gcd)
    # print(m, n, x, y, gcd, lcm)
    result = -1
    if m == x and n == y :
        result = lcm
    cnt = int(lcm / m)
    # print("cnt", cnt)
    first = x
    if first > n:
        first = first % n
        if not first :
            first = y
    # print(first)

    for month in range(cnt):
        if first == y :
            result = (month) * m + x
            break
        first += m
        if first > n:
            first = first % n
            if not first:
                first = n




    print(result)
