import sys
sys.stdin = open("workshop2.txt")

def BFS(g, start, depth):
    global n
    Q = []
    Q.append(start)
    visited[start] = 1
    check = start
    check_list = []
    while Q:
        # print(Q, depth)
        t = Q.pop(0)
        for i in range(n):
            if g[t][i] and not visited[i]:
                Q.append(i)
                visited[i] = 1
                check_list.append(i)
        if Q and check == t:
            depth += 1
            check = Q[-1]
            result_list = check_list[:]
            check_list = []
    # print(result_list)
    return result_list


for tc in range(10):
    n, start = map(int, input().split())
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    data = list(map(int, input().split()))
    total = len(data) // 2
    visited = [0 for _ in range(n + 1)]
    for i in range(total):
        row, col = data[i * 2], data[i * 2 + 1]
        graph[row][col] = 1


    result = BFS(graph, start, 0)

    # for i in graph:
    #     print(i)
    print("#{} {}".format(tc + 1, max(result)))