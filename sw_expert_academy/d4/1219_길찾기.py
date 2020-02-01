import sys
sys.stdin = open("1219_input.txt")

def bfs():
    while Q:
        now = Q.pop(0)
        for i in range(100):
            if Map[now][i] and not visited[i]:
                if i == 99:
                    return 1
                Q.append(i)
                visited[i] = 1
    return 0


for tc in range(10):
    t, n = map(int, input().split())
    temp = list(map(int, input().split()))
    Map = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(n):
        s, e = temp[i * 2], temp[i * 2 + 1]
        Map[s][e] = 1
    visited = [0 for _ in range(100)]
    Q = []

    for i in range(100):
        if Map[0][i]:
            Q.append(i)
            visited[i] = 1
    # print(Q)


    print(f"#{tc + 1} {bfs()}")
    # print(Map)