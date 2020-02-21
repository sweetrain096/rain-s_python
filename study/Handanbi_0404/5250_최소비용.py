import sys
sys.stdin = open("5250_input.txt")

# deg = ((1, 0), (0, 1), (-1, 0), (0, -1))
#
# def is_wall(r, c):
#     if r < 0 or r >= n or c < 0 or c >= n:
#         return True
#
# def inque(a):
#     global wp
#     Q[wp] = a
#     wp += 1
#
# def bfs():
#     global rp, wp
#     bfs_data[0][0] = 0
#     Q.append([0, 0, 0])
#     # inque([0, 0, 0])
#
#
#     while Q:
#
#         # tr, tc, t_fuel = Q[rp]
#         tr, tc, t_fuel = Q.pop(0)
#         rp += 1
#         for dr, dc in deg:
#             nr, nc = dr + tr, dc + tc
#             if not is_wall(nr, nc):
#                 if data[tr][tc] < data[nr][nc]:
#                     plus_fuel = data[nr][nc] - data[tr][tc]
#                 else:
#                     plus_fuel = 0
#
#                 if bfs_data[nr][nc] > plus_fuel + bfs_data[tr][tc] + 1:
#                     Q.append([nr, nc, plus_fuel + bfs_data[tr][tc] + 1])
#                     # inque([nr, nc, plus_fuel + t_fuel + 1])
#                     bfs_data[nr][nc] = plus_fuel + bfs_data[tr][tc] + 1
#     return bfs_data[n - 1][n - 1]
#
#
#
#
# t = int(input())
# for tc in range(t):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#
#     bfs_data = [[9999999 for _ in range(n)] for _ in range(n)]
#     Q = []
#     rp, wp = 0, 0
#
#
#
#     print("#{} {}".format(tc + 1, bfs()))
#     # for i in bfs_data:
#     #     print(i)
#





deg = ((1, 0), (0, 1), (-1, 0), (0, -1))

def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True

def inque(a):
    global wp
    Q[wp] = a
    wp += 1

def bfs():
    global rp, wp
    bfs_data[0][0] = 0
    inque([0, 0])


    while rp < wp:
        if wp >= 100000:
            return bfs_data[n - 1][n - 1]
        tr, tc = Q[rp]
        rp += 1
        for dr, dc in deg:
            nr, nc = dr + tr, dc + tc
            if not is_wall(nr, nc):
                if data[tr][tc] < data[nr][nc]:
                    plus_fuel = data[nr][nc] - data[tr][tc]
                else:
                    plus_fuel = 0

                if bfs_data[nr][nc] > plus_fuel + bfs_data[tr][tc] + 1:
                    inque([nr, nc])
                    bfs_data[nr][nc] = plus_fuel + bfs_data[tr][tc] + 1
    return bfs_data[n - 1][n - 1]





for tc in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    bfs_data = [[9999999 for _ in range(n)] for _ in range(n)]
    Q = [0] * 100000
    rp, wp = 0, 0



    print("#{} {}".format(tc + 1, bfs()))

