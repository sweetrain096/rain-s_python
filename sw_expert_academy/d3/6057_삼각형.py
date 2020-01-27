import sys
sys.stdin = open("6057_input.txt")

for tc in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(graph)

    idx = 1
    for i in range(1, n + 1):
        if graph[i]:
            idx = i
            break

    while True:
        v = idx
        flag = True
        for i in range(3):
            print("v", v)
            Next = graph[v].pop()
            print(Next, graph)
            graph[Next].remove(v)
            print(graph)
            if not graph[Next]:
                flag = False
                break

            v = graph[Next].pop()
            print(Next, v)

        break
