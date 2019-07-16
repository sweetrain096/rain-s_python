import sys
sys.stdin = open("최소신장트리_input.txt")

def make_mst():
    start_node = 0      # 시작점을 0으로 설정
    D[start_node] = 0   # 시작점이 0이기 때문에 가중치 0
    result = 0          # 최소 이동거리 초기화

    for cnt in range(node_total + 1):   # 반복 횟수 노드의 개수만큼
        min_weight = 9999999
        for v in range(node_total + 1):
            if not visited[v] and min_weight > D[v]:
                min_weight = D[v]
                start_node = v

        visited[start_node] = 1
        result += graph[pi[start_node]][start_node]


        for v in range(node_total + 1):
            if graph[start_node][v] and not visited[v] and graph[start_node][v] < D[v]:
                D[v] = graph[start_node][v]
                pi[v] = start_node

    return result

for tc in range(int(input())):
    node_total, edge_total = map(int, input().split())
    graph = [[0 for _ in range(node_total + 1)] for _ in range(node_total + 1)]

    D = [9999999] * (node_total + 1)    # 가중치 최솟값 저장
    pi = list(range(node_total + 1))    # 부모 저장
    visited = [0] * (node_total + 1)    # 방문처리

    for i in range(edge_total):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w



    # for i in graph:
    #     print(i)

    print("#{} {}".format(tc + 1, make_mst()))

