import sys
sys.stdin = open("1861_input.txt")


deg = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False


def dfs(r, c):
    global new_cnt, new_min
    visited[r][c] = 1
    if new_min > Map[r][c]:
        new_min = Map[r][c]
    new_cnt += 1
    for dr, dc in deg:
        nr = r + dr
        nc = c + dc
        if not is_wall(nr, nc) and not visited[nr][nc] and abs(Map[r][c] - Map[nr][nc]) == 1:
            dfs(nr, nc)



for tc in range(int(input())):
    n = int(input())
    Map = []
    visited = [[0 for _ in range(n)] for _ in  range(n)]
    Min = n * n
    cnt = 0
    for i in range(n):
        temp = list(map(int, input().split()))
        Map.append(temp)

    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                new_min = n * n
                new_cnt = 0
                dfs(r, c)
                # print("nm, nc", new_min, new_cnt)
                if cnt < new_cnt:
                    cnt = new_cnt
                    Min = new_min
                elif cnt == new_cnt:
                    if Min > new_min:
                        Min = new_min

    # print(Map)
    print(f"#{tc + 1} {Min} {cnt}")