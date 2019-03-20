import sys
sys.stdin = open("11724_input.txt")

from collections import deque

def bfs(v):
    global cnt
    Q = deque([v])
    visited[v] = 1

    while Q:
        t = Q.popleft()
        for i in range(n):
            if graph[t][i]:
                Q.append(i)
                visited[i] = 1
                graph[t][i] = 0
                graph[i][t] = 0

    cnt += 1


n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = 1
    graph[v - 1][u - 1] = 1
#
# for i in graph:
#     print(i)

cnt = 0
visited = [0] * n
for v in range(n):
    if not visited[v]:
        bfs(v)
print(cnt)
# for row in range(n):
#     for col in range(n):
#         if graph[row][col]:
#             bfs(row, col)