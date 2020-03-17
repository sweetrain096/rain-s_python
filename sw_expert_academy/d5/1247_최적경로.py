import sys
sys.stdin = open("1247_input.txt")


def find(start, distance, cnt):
    global Min
    if cnt == n:
        if distance + Map[start][-1] < Min:
            Min = distance + Map[start][-1]
        return

    for i in range(1, n+1):
        if start != i and not visited[i] and distance + Map[start][i] < Min:
            visited[i] = 1
            find(i, distance + Map[start][i], cnt + 1)
            visited[i] = 0


for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    office = (data[0], data[1])
    home = (data[2], data[3])
    data_x = [office[0]]
    data_y = [office[1]]
    for i in range(2, n+2):
        data_x.append(data[i * 2])
        data_y.append(data[i * 2 + 1])
    data_x.append(home[0])
    data_y.append(home[1])
    Map = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    visited = [0 for _ in range(n+2)]

    for i in range(n + 2):
        for j in range(n + 2):
            dist = abs(data_x[i] - data_x[j]) + abs(data_y[i] - data_y[j])
            Map[i][j] = dist
            Map[j][i] = dist


    Min = 0
    for i in range(n + 1):
        Min += Map[i][i + 1]


    for i in range(1, n + 1):
        visited[i] = 1
        find(i, Map[0][i], 1)
        visited[i] = 0



    print(f"#{tc + 1} {Min}")