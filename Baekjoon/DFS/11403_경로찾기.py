import sys
sys.stdin = open("11403_input.txt")

def dfs(node):
    global cnt
    if cnt:
        visited[node] = 1
    cnt += 1
    for i in range(n):
        if graph[node][i] and not visited[i]:
            dfs(i)



n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

for row in range(n):
    visited = [0 for _ in range(n)]
    cnt = 0
    dfs(row)
    print(' '. join(map(str, visited)))

