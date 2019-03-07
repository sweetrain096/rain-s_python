import sys
sys.stdin = open("1260_input.txt")


def dfs(node):
    visited_dfs[node] = 1
    result_dfs.append(node)
    if node:
        for i in range(1, n + 1):
            if graph[node][i] and not visited_dfs[i]:
                dfs(i)

def bfs(node):
    result = []
    Q = [node]
    visited_bfs[node] = 1
    while Q:
        t = Q.pop(0)
        result.append(t)
        for i in range(1, n + 1):
            if graph[t][i] and not visited_bfs[i]:
                Q.append(i)
                visited_bfs[i] = visited_bfs[t] + 1
    return result




n, m, v = map(int, input().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited_dfs = [0 for _ in range(n + 1)]
result_dfs = []
visited_bfs = [0 for _ in range(n + 1)]
for i in range(m):
    now, num = map(int, input().split())
    graph[now][num] = 1
    graph[num][now] = 1

# for i in graph:
#     print(i)

dfs(v)
result_bfs = bfs(v)

print(' '.join(map(str, result_dfs)))
print(' '.join(map(str, result_bfs)))