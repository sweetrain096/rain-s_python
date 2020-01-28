import sys
sys.stdin = open("6057_input.txt")


def make_triangle(start, mid):
    global cnt
    for i in range(mid + 1, n + 1):
        if graph[mid][i]:
            if graph[i][start]:
                end = i
                able = tuple(sorted([start, mid, end]))
                if not make.get(able):
                    make[able] = 1
                    cnt += 1


for tc in range(int(input())):
    n, m = map(int, input().split())
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    make = dict()
    cnt = 0
    for i in range(m):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    for r in range(1, n + 1):
        for c in range(r + 1, n + 1):
            if graph[r][c]:
                make_triangle(r, c)
            # print(r, c, cnt)
    print(f"#{tc + 1} {cnt}")