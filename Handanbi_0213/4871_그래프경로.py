import sys
sys.stdin = open("4871_input.txt")

def dfs(s, g):

    visited[s] = 1
    result.append(s)

    cnt = 0
    for w in range(1, v + 1):
        if graph[s][w] == 1 and visited[w] == 0:
            dfs(w, g)
        if not graph[s][w]:
            cnt += 1

    if g in result:
        return 1
    if cnt == v:
        result.pop()



for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[0 for i in range(v + 1)] for j in range(v + 1)]

    for i in range(e):
        row, col = map(int, input().split())
        graph[row][col] = 1

    s, g = map(int, input().split())

    stack = []
    visited = [0 for i in range(v + 1)]
    result = []

    save = dfs(s, g)
    if save == None:
        save = 0



    print(f"#{tc + 1} {save}")