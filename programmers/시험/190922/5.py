import sys
sys.stdin = open("5_input.txt")

# 어차피 코니는 문보다 r, c 가 큰 곳에만 있기 때문
deg = [(1, 0), (0, 1)]

def is_wall(in_r, in_c):
    if in_r < 0 or in_r >= r or in_c < 0 or in_c >= c:
        return True
    return False

def catch_coni(cr, cc):
    if is_wall(cr, cc):
        return False

    Q = []
    Q.append((0, 0))
    cnt_check[0][0] = 1
    while Q:
        mr, mc = Q.pop(0)
        for dr, dc in deg:
            nr, nc = mr + dr, mc + dc
            if not is_wall(nr, nc):
                if not time_check[nr][nc]:
                    Q.append((nr, nc))
                    time_check[nr][nc] = time_check[mr][mc] + 1
                    cnt_check[nr][nc] = cnt_check[mr][mc]
                elif time_check[nr][nc] == time_check[mr][mc] + 1:
                    cnt_check[nr][nc] += cnt_check[mr][mc]
    return time_check[cr][cc], cnt_check[cr][cc]


r, c = map(int, (input().split()))
cr, cc = map(int, input().split())

time_check = [[0 for _ in range(c)] for _ in range(r)]
cnt_check = [[0 for _ in range(c)] for _ in range(r)]

time, cnt = catch_coni(cr, cc)
print(time)
print(cnt)