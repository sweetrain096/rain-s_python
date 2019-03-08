import sys
sys.stdin = open("7576_input.txt")
from collections import deque

def bfs():
    Q = deque(start)
    stack = start[:]
    for row, col in Q:
        visited[row][col] += 1
    while Q:
        t = Q.popleft()
        # print(stack)
        # for i in visited:
        #     print(i)
        # print()
        if len(stack) == total:
            result = 0
            for row in range(n):
                result = max(result, max(visited[row]))
            return result - 1
        for pr, pc in deg:
            r, c = t[0] + pr, t[1] + pc
            if r >= 0 and r < n and c >= 0 and c < m:
                if not box[r][c] and not visited[r][c]:
                    Q.append([r, c])
                    stack.append([r, c])
                    visited[r][c] += visited[t[0]][t[1]] + 1
    return -1

m, n = map(int, input().split())
box, start = [], []
visited = [[0 for _ in range(m)] for _ in range(n)]
deg = [[-1, 0], [0, 1], [1, 0], [0, -1]]
none_place = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)
    for j in range(m):
        if tmp[j] == 1:
            start.append([i, j])
        elif tmp[j] == -1:
            none_place += 1
total = m * n - none_place

print(bfs())











# def iswall(r, c):
#     if r < 0 or r >= n or c < 0 or c >= m:
#         return True
#
# def bfs():
#     Q = deque(toma_list[:])
#     t = Q[0]
#     visited[t[0]][t[1]] = 1
#     stack = toma_list[:]
#     while Q:
#         t = Q.popleft()
#
#         for i in range(4):
#             if not iswall(t[0] + deg[i][0], t[1] + deg[i][1]) and not data[t[0] + deg[i][0]][t[1] + deg[i][1]]:
#                 Q.append([t[0] + deg[i][0], t[1] + deg[i][1]])
#                 if not visited[t[0] + deg[i][0]][t[1] + deg[i][1]]:
#                     visited[t[0] + deg[i][0]][t[1] + deg[i][1]]= visited[t[0]][t[1]] + 1
#                 data[t[0] + deg[i][0]][t[1] + deg[i][1]] = 1
#                 stack.append([t[0] + deg[i][0], t[1] + deg[i][1]])
#
#     if len(stack) == total:
#         result = 0
#         for j in visited:
#             check = max(j)
#             if result < check:
#                 result = check
#         return result - 1
#     return -1
#
#
#
# m, n = map(int, input().split())
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# visited = [[0 for _ in range(m)] for _ in range(n)]
# total = 0
#
# toma_list = []
# deg = [[0, -1], [1, 0], [0, 1], [-1, 0]]
# for row in range(n):
#     for col in range(m):
#         if data[row][col] != -1:
#             total += 1
#             if data[row][col] == 1:
#                 toma_list.append([row, col])
#
# print(bfs())





# def iswall(r, c):
#     if r < 0 or r >= n or c < 0 or c >= m:
#         return True
#
# def bfs(min):
#     Q = toma_list[:]
#     check = Q[-1]
#     day = 0
#     while Q:
#
#         t = Q.pop(0)
#         for i in range(4):
#             if not iswall(t[0] + deg[i][0], t[1] + deg[i][1]) and not data[t[0] + deg[i][0]][t[1] + deg[i][1]]:
#                 Q.append([t[0] + deg[i][0], t[1] + deg[i][1]])
#                 data[t[0] + deg[i][0]][t[1] + deg[i][1]] = 1
# def bfs():
#     Q = toma_list[:]
#     check = Q[-1]
#     day = 0
#     stack = Q[:]
#     if len(stack) == total:
#         return 0
#     while Q:
#         t = Q.pop(0)
#         # print(len(stack), total, "stack", stack)
#         if len(stack) == total:
#             if Q:
#                 day += 1
#             # print("day", day)
#             return day
#
#         for i in range(4):
#             if not iswall(t[0] + deg[i][0], t[1] + deg[i][1]) and not data[t[0] + deg[i][0]][t[1] + deg[i][1]]:
#                 Q.append([t[0] + deg[i][0], t[1] + deg[i][1]])
#                 stack.append([t[0] + deg[i][0], t[1] + deg[i][1]])
#                 data[t[0] + deg[i][0]][t[1] + deg[i][1]] = 1
#
#
#         # print(Q)
#         # print(t, check)
#         if t == check:
#             day += 1
#
#             if Q:
#                 check = Q[-1]
#
#         cnt = 0
#         for i in data:
#             cnt += sum(i)
#         #     print(i)
#         # print(day, cnt, min)
#         if cnt + min == total:
#             if len(Q) > 1:
#                 return day + 1
#             return day
#
#             # check = Q[-1]
#             if Q:
#                 check = Q[-1]
#
#         # cnt = 0
#         # for i in data:
#         #     cnt += sum(i)
#         #     print(i)
#         # print("day222", day, cnt)
#         # if cnt + min == total:
#         #     if len(Q) > 1:
#         #         return day + 1
#         #     return day
#
#
#     return -1
#
#
#
# m, n = map(int, input().split())
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# total = 0
#
# toma_list = []
# deg = [[0, -1], [1, 0], [0, 1], [-1, 0]]
# for row in range(n):
#     for col in range(m):
#         if data[row][col] != -1:
#             total += 1
#             if data[row][col] == 1:
#                 toma_list.append([row, col])
#
# min = m * n - total
# # print(total)
# # print(toma_list)
# # print(min)
# #
# # print("result")
# print(bfs())
#
# #
# # for i in data:
# #     print(i)
#
#
# print(bfs())
#
