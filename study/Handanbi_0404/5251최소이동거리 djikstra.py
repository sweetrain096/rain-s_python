import sys
sys.stdin = open("최소이동거리_input.txt")

def djikstra(start_node):
    key[start_node] = 0
    result = 0

    for i in range(end_node + 1):
        min_weight = 9999999
        for v in range(end_node + 1):
            if not visited[v] and min_weight > (key[v]):
                min_weight = key[v]
                start_node = v
        visited[start_node] = 1

        for v in range(end_node + 1):
            if graph[start_node][v] and not visited[v] and graph[start_node][v] + key[start_node] < key[v]:
                key[v] = graph[start_node][v] + key[start_node]
                parent[v] = start_node


    return key[end_node]


for tc in range(int(input())):
    end_node, edge_total = map(int, input().split())
    graph = [[0 for _ in range(end_node + 1)] for _ in range(end_node + 1)]

    for i in range(edge_total):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    key = [9999999] * (end_node + 1)
    parent = list(range(end_node + 1))
    visited = [0] * (end_node + 1)

    # for i in graph:
    #     print(i)

    print("#{} {}".format(tc + 1, djikstra(0)))