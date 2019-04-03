import sys
sys.stdin = open("최소신장트리_input.txt")

def make_mst(start_node):

    mst[start_node][0] = 0
    mst[start_node][1] = start_node
    new_node = start_node

    for cnt in range(node_total + 1):
        min_weight = 9999999
        visited[start_node] = 1

        for i in range(node_total + 1):
            # print(new_node, graph[start_node][i])
            if not visited[i] and graph[start_node][i]:
                if mst[i][0] > graph[start_node][i]:
                    mst[i][0] = graph[start_node][i] # 가중치 저장
                    mst[i][1] = start_node
                if min_weight > graph[start_node][i] and graph[start_node][i]:
                    min_weight = graph[start_node][i]
                    new_node = i
        start_node = new_node
    result = 0
    for i in mst:
        result += i[0]

    return result

for tc in range(int(input())):
    node_total, edge_total = map(int, input().split())
    graph = [[0 for _ in range(node_total + 1)] for _ in range(node_total + 1)]
    mst = [[9999999, i] for i in range(node_total + 1)]
    tree = []
    for i in range(edge_total):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w

    visited = [0] * (node_total + 1)

    print("#{} {}".format(tc + 1, make_mst(0)))

