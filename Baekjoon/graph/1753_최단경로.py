import sys

sys.stdin = open("1753_input.txt")
V, E = map(int, input().split())
print(V, E)
K = int(input())
visited = [0 for i in range(V+1)]
distance = [99999 for i in range(V+1)]
s = []


def djikstra(start_node):
    s.append(start_node)
    visited[start_node] = 1
    distance[start_node] = 0

    for i in range(1, V+1):
        if not visited[i] and graph[start_node][i]:
            if distance[start_node] + graph[start_node][i] < distance[i]:
                distance[i] = distance[start_node] + graph[start_node][i]





graph = [[0 for i in range(V+1)] for j in range(V+1)]
for i in range(0, E):
    u, v, w = map(int, input().split())
    graph[u][v] = w

for i in range(1, V+1):
    for j in range(1, V+1):
        print(graph[i][j], end=" ")
    print()


