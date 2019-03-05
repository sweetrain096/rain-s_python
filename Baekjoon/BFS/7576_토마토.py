import sys
sys.stdin = open("7576_input.txt")

def iswall(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return True

def bfs():
    Q = toma_list[:]
    check = Q[-1]
    day = 0
    stack = Q[:]
    if len(stack) == total:
        return 0
    while Q:
        t = Q.pop(0)
        # print(len(stack), total, "stack", stack)
        if len(stack) == total:
            if Q:
                day += 1
            # print("day", day)
            return day

        for i in range(4):
            if not iswall(t[0] + deg[i][0], t[1] + deg[i][1]) and not data[t[0] + deg[i][0]][t[1] + deg[i][1]]:
                Q.append([t[0] + deg[i][0], t[1] + deg[i][1]])
                stack.append([t[0] + deg[i][0], t[1] + deg[i][1]])
                data[t[0] + deg[i][0]][t[1] + deg[i][1]] = 1

        # print(Q)
        # print(t, check)
        if t == check:
            day += 1
            # check = Q[-1]
            if Q:
                check = Q[-1]

        # cnt = 0
        # for i in data:
        #     cnt += sum(i)
        #     print(i)
        # print("day222", day, cnt)
        # if cnt + min == total:
        #     if len(Q) > 1:
        #         return day + 1
        #     return day

    return -1



m, n = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

total = 0

toma_list = []
deg = [[0, -1], [1, 0], [0, 1], [-1, 0]]
for row in range(n):
    for col in range(m):
        if data[row][col] != -1:
            total += 1
            if data[row][col] == 1:
                toma_list.append([row, col])

print(bfs())
