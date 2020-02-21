import sys
sys.stdin = open("5248_input.txt")

def make(start_node):
    global cnt, flag, no

    visited[start_node] = 1

    if not sum(graph[start_node]):
        no += 1
        return

    for i in range(1, n + 1):
        if graph[start_node][i] and not visited[i]:
            visited[i] = 1
            make(i)
    if flag == 1:
        return
    if visited[start_node]:
        # cnt += 1
        flag = 1
        return



for tc in range(int(input())):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for i in range(m):
        graph[tmp[i * 2]][tmp[i * 2 + 1]] = 1
        graph[tmp[i * 2 + 1]][tmp[i * 2]] = 1

    cnt = 0
    no = 0
    for i in range(1, n + 1):
        flag = 0
        if not visited[i]:
            make(i)
        if flag:
            cnt += 1
    if no:
        cnt += no

    print("#{} {}".format(tc + 1, cnt))
