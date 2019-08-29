import sys
sys.stdin = open("1260_input.txt")

def DFS(v):
    for i in range(1, n+1):
        if not visited_dfs[i] and Map[v][i]:
            visited_dfs[i] = 1
            result_dfs.append(i)
            DFS(i)

def BFS(v):
    result = []
    Q = [v]
    visited_bfs[v] = 1
    while Q:
        now = Q.pop(0)
        result.append(now)
        for i in range(1, n+1):
            if not visited_bfs[i] and Map[now][i]:
                Q.append(i)
                visited_bfs[i] = 1
    return result


n, m, v = list(map(int, input().split()))
Map = [[0 for i in range(n+1)] for j in range(n+1)]
visited_dfs = [0 for i in range(n+1)]
result_dfs = []
visited_bfs = [0 for i in range(n+1)]
for i in range(m):
    x, y = list(map(int, input().split()))
    Map[x][y] = 1
    Map[y][x] = 1

visited_dfs[v] = 1
result_dfs.append(v)
DFS(v)
print(' '.join(map(str, result_dfs)))
print(' '.join(map(str, BFS(v))))