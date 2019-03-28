import sys
sys.stdin = open("5202_input.txt")

def dfs(k, cnt_check):
    global result
    if cnt_check + (total - k - 1) < result:
        return

    if k == total - 1:
        result = max(result, cnt_check)
        return

    e = data[k][1]

    for i in range(k + 1, total):
        if data[i][0] >= e:
            dfs(i, cnt_check + 1)





for tc in range(int(input())):
    n = int(input())

    tmp = []
    for i in range(n):
        tmp.append(list(map(int, input().split())))

    tmp.sort()

    data = [tmp[0]]
    for i in range(1, n):
        if tmp[i][0] != data[-1][0]:
            data.append(tmp[i])
    print(data)
    total = len(data)
    result = 0
    for i in range(total):
        dfs(i, 1)


    print("#{} {}".format(tc + 1, result))