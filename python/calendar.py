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
    result = -1
    if m <= n :
        cnt = int(m / GCD(n, m))
        first = x
        for month in range(cnt):
            if first == y :
                break
            first -= (n - m)
            if first <= 0:
                first += n
        result = (cnt - 1) * m + x
    #     calendar_lists = [[i] for i in range(1, m + 1)]
    #
    #
    #     for i in range(m):
    #         for j in range(cnt):
    #             if calendar_lists[i][j] - (n - m) <= 0 :
    #                 new_n = calendar_lists[i][j] - (n - m) + n
    #             else:
    #                 new_n = calendar_lists[i][j] - (n - m)
    #             calendar_lists[i].append(new_n)
    #     if y in calendar_lists[x - 1] :
    #         # print("ok")
    #         result = ((calendar_lists[x + 1].index(y) - 1) * m) +  calendar_lists[x - 1].index(y)
    #
    # else :
    #     calendar_lists = []
    #     cnt = int(n / GCD(m, n))
    #     j = 0
    #     # print("m", m)
    #     for i in range(1, m+1) :
    #         j += 1
    #         # print("n", n)
    #         if j > n :
    #             j -= n
    #         calendar_lists.append([j])
    #
    #     for i in range(m):
    #         for j in range(cnt - 1):
    #             if calendar_lists[i][j] - (n - m) >= (n + 1):
    #                 new_n = calendar_lists[i][j] - (n - m) - n
    #             else:
    #                 new_n = calendar_lists[i][j] - (n - m)
    #             calendar_lists[i].append(new_n)
    #     if y in calendar_lists[x - 1] :
    #         # print("ok")
    #         # print(calendar_lists)
    #         # print((calendar_lists[x - 1].index(y)))
    #         result = ((calendar_lists[x - 1].index(y)) * m) +  n - x -1

    print(result)
