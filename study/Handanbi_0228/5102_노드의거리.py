import sys
sys.stdin = open("5102_input.txt")




def BFS(graph, s, g, depth):
    global v
    Q = []
    visited = [0 for _ in range(v)]
    Q.append(s - 1)
    visited[s - 1] = 1
    check = Q[-1]
    # print(Q)
    while Q:

        t = Q.pop(0)
        if t == g - 1:
            return depth
        # print(t, graph[t])
        for i in range(v):
            # print(graph[t][i])
            # print(i)
            if graph[t][i] and not visited[i]:
                Q.append(i)
                visited[i] = 1
        if Q and t == check:
            depth += 1
            check = Q[-1]
        # print(Q)
    if not Q:
        return 0








for tc in range(int(input())):
    v, e = map(int, input().split())
    table = [[0 for _ in range(v)] for _ in range(v)]
    for i in range(e):
        num1, num2 = map(int, input().split())
        table[num1 - 1][num2 - 1] = 1
        table[num2 - 1][num1 - 1] = 1
    s, g = map(int, input().split())


    result = BFS(table, s, g, 0)


    # for i in table:
    #     print(i)

    print(f"#{tc + 1} {result}")