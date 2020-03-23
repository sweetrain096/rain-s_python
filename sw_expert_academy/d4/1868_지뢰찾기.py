import sys
sys.stdin = open("1868_input.txt")

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False

def find(r, c, cnt):
    Q = []
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        tr, tc = Q.pop(0)
        mine_cnt = 0

        for i in range(8):
            nr = tr + dr[i]
            nc = tc + dc[i]
            if not is_wall(nr, nc):
                if Map[nr][nc] == '*':
                    mine_cnt += 1
        if not mine_cnt:
            for i in range(8):
                nr = tr + dr[i]
                nc = tc + dc[i]
                if not is_wall(nr, nc) and not visited[nr][nc] and Map[nr][nc] == '.':
                    Q.append((nr, nc))
                    visited[nr][nc] = 1

        Map[tr][tc] = mine_cnt


    return cnt + 1


for tc in range(int(input())):
    n = int(input())
    Map = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        tmp = []
        for i in input():
            tmp.append(i)
        Map.append(tmp)
    cnt = 0

    for i in range(n):
        for j in range(n):
            if Map[i][j] != '.':
                continue
            mine = 0
            for k in range(8):
                nr = i + dr[k]
                nc = j + dc[k]
                if not is_wall(nr, nc) and Map[nr][nc] == '*':
                    mine += 1
            if not mine:
                cnt = find(i, j, cnt)
    for i in range(n):
        for j in range(n):
            if Map[i][j] == '.':
                cnt += 1

    # for i in range(n//2 + 1):
    #     for j in range(n//2 + 1):
    #         # print(i, j, n - i - 1, n - j - 1)
    #         if Map[i][j] == '.':
    #             cnt = find(i, j, cnt)
    #         if Map[n - i - 1][j] == '.':
    #             cnt = find(n - i - 1, j, cnt)
    #         if Map[i][n - j - 1] == '.':
    #             cnt = find(i, n - j - 1, cnt)
    #         if Map[n - i - 1][n - j - 1] == '.':
    #             cnt = find(n - i - 1, n - j - 1, cnt)

    print(f"#{tc + 1} {cnt}")