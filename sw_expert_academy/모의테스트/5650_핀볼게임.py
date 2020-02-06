import sys
sys.stdin = open("5650_input.txt")

# <dir> 좌 : 0, 상 : 1, 우 : 2, 하 : 3
deg = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False

def find_hole(r, c):
    for i in range(n):
        for j in range(n):
            if Map[i][j] == Map[r][c]:
                if i != r or j != c:
                    return i, j


def run_game(r, c, dir):
    cnt = 0
    dr, dc = deg[dir]
    nr = r
    nc = c
    while True:
        nr += dr
        nc += dc
        # 종료 조건
        if nr == r and nc == c:
            return cnt
        # 가장자리 벽에 부딪혔을 때
        if is_wall(nr, nc):
            dir = (dir + 2) % 4
            dr, dc = deg[dir]
            cnt += 1
            continue
        # print("MAP", Map[nr][nc], nr, nc, dir)

        # 아무것도 없을 때
        if not Map[nr][nc]:
            continue

        # 블록들을 만날 때
        if Map[nr][nc] >= 1 and Map[nr][nc] <= 5:
            cnt += 1
            if visited.get((nr, nc)):
                if dir in visited.get((nr, nc)):
                    return -1
            visited[nr, nc] = [dir]
            # 1번 블록을 만날 때
            if Map[nr][nc] == 1:
                # 왼쪽 방향일 때
                if not dir:
                    dir = 1
                # 아래 방향일 때
                elif dir == 3:
                    dir = 2
                # 다른 두 방향일 때
                else:
                    dir = (dir + 2) % 4

            # 2번 블록을 만날 때
            elif Map[nr][nc] == 2:
                # 왼쪽 방향일 때
                if not dir:
                    dir = 3
                # 위쪽 방향일 때
                elif dir == 1:
                    dir = 2
                else:
                    dir = (dir + 2) % 4

            # 3번 블록을 만날 때
            elif Map[nr][nc] == 3:
                # 오른쪽 방향일 때
                if dir == 2:
                    dir = 3
                # 위쪽 방향일 때
                elif dir == 1:
                    dir = 0
                else:
                    dir = (dir + 2) % 4

            # 4번 블록을 만날 때
            elif Map[nr][nc] == 4:
                # 오른쪽 방향일 때
                if dir == 2:
                    dir = 1
                # 아래 방향일 때
                elif dir == 3:
                    dir = 0
                else:
                    dir = (dir + 2) % 4

            # 5번 블록을 만날 때
            elif Map[nr][nc] == 5:
                # 모든 방향 바뀜
                dir = (dir + 2) % 4

            dr, dc = deg[dir]

        # 블랙홀을 만날 때
        elif Map[nr][nc] == -1:
            return cnt

        # 웜홀을 만날 때
        else:
            # 같은 번호의 다른 웜홀 찾기
            # print(nr, nc, find_hole(nr, nc))
            nr, nc = find_hole(nr, nc)









for tc in range(int(input())):
    n = int(input())
    Map = []
    visited = dict()
    for i in range(n):
        temp = list(map(int, input().split()))
        Map.append(temp)
    CNT = 0
    for r in range(n):
        for c in range(n):
            if not Map[r][c]:
                for i in range(4):
                    visited.clear()
                    temp = run_game(r, c, i)
                    # print(r, c, i, temp)
                    if temp > CNT:
                        CNT = temp

    print(f"#{tc + 1} {CNT}")