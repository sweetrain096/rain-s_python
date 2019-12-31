import sys
sys.stdin = open("2252_input.txt")

n, m = map(int, input().split())
Graph = [[] for _ in range(n + 1)]
E = [0 for _ in range(n + 1)]

for i in range(m):
    start, end = map(int, input().split())
    E[end] += 1
    Graph[start].append(end)

# print(Graph)
Q = []
result = []

for i in range(1, n + 1):
    if not E[i]:
        Q.append(i)

while Q:
    node = Q.pop(0)
    result.append(node)

    for v in range(len(Graph[node])):
        V = Graph[node][v]
        E[V] -= 1
        if not E[V]:
            Q.append(V)





print(' '.join(map(str, result)))