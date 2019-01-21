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
    # print(m, n, x, y)
    result = -1
    if m <= n :
        cnt = int(n / GCD(n, m))
        first = x

        for month in range(cnt):
            if first == y :
                break
            first -= (n - m)
            if first <= 0:
                first += n
        result = (month) * m + x
        if month + 1 == cnt and first != y:
            result = -1


    else:
        cnt = int(n / GCD(m, n))
        first = x

        if first > n :
            first -= n

        for month in range(cnt):
            if first == y:
                break
            first += (m - n)
            # plus += 1
            if first > n:
                first -= n
        result = (month) * m + x
        if month + 1 == cnt and first != y:

            result = -1




    print(result)
