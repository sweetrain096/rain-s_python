import sys
sys.stdin = open("workshop2_input.txt")


for cn in range(10):
    V, E = map(int, input().split()) # V는 정점의 갯수, E는 노드의 갯수
    n = list(map(int, input().split()))
    G = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(E):
        G[n[2*i +1] - 1][n[2*i] - 1] = 1
        line = []
    while(1):
        for i in range(1,V+1):
            if sum(G[i-1]) == 0 and str(i) not in line:
                line.append(str(i))
                for j in range(1,V+1):
                    G[j-1][i-1] = 0
        if len(line) == V:
            break
    result = ' '.join(line)
    print(f"#{cn+1} {result}")




# for tc in range(10):
#     v, e = map(int, input().split())
#     tmp = list(map(int, input().split()))
#     graph = [[0 for i in range(v + 1)] for j in range(v + 1)]
#     visited = [0 for i in range(v + 1)]
#
#     for cnt in range(e):
#         row, col = tmp[cnt * 2 : (cnt + 1) * 2]
#         # print(row, col)
#         graph[row][col] = 1
#     # print(tmp)
#
#
#     stack = []
#     result = []
#
#     for row in range(1, v + 1):
#         check = 0
#         for col in range(1, v + 1):
#             if graph[col][row]:
#                 check = 1
#                 break
#         if not check:
#             stack.append(row)
#
#     while stack:
#         # print("stack", stack)
#         # print("result", result)
#         # print("visited", visited)
#         node = stack.pop()
#         if not visited[node]:
#
#             for col in range(1, v + 1):
#                 if graph[node][col]:
#
#                     stack.append(col)
#             check = []
#             for row in range(1, v + 1):
#                 if graph[row][node]:
#                     check.append(row)
#
#             # print("node", node, check)
#             if not check:
#                 result.append(node)
#                 visited[node] = 1
#             else:
#                 cnt = 0
#                 for check_one in check:
#                     if visited[check_one]:
#                         cnt += 1
#
#                 if cnt == len(check):
#                     result.append(node)
#                     visited[node] = 1
#
#
#
#     # for graph1 in graph:
#     #     print(graph1)
#     print(f"#{tc + 1} {' '.join(map(str, result))}")




