import sys
sys.stdin = open("최소이동거리_input.txt")

for tc in range(int(input())):
    end_node, edge_total = map(int, input().split())
    graph = [[0 for _ in range(end_node + 1)] for _ in range(end_node + 1)]

    for i in range(edge_total):
        s, e, w = map(int, input().split())
        graph[s][e] = w


