import sys
sys.stdin = open("2468_input.txt")

import copy


deg = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Q = []
def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False

def bfs(rain, Map):
    cnt = -1
    for r in range(n):
        for c in range(n):
            if Map[r][c] > rain:
                print(r, c)
                Q.append([r, c])
                while Q:
                    tr, tc = Q.pop(0)
                    Map[tr][tc] = cnt
                    for dr, dc in deg:
                        nr = tr + dr
                        nc = tc + dc
                        if not is_wall(nr, nc) and not Map[nr][nc]:
                            Q.append([nr, nc])
                cnt -= 1
    return -cnt - 1

# def rainning(rain, Map):
#     for r in range(n):
#         for c in range(n):
#             if Map[r][c] <= rain:
#                 Map[r][c] = -1
#             else:
#                 Map[r][c] = 0
#
#     a = bfs(Map)
#     return a

n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
final = 1
for line in Map:
    final = max(final, max(line))
safe = 1

for rain in range(2, 101):
    if rain > final:
        break
    safe = max(safe, bfs(rain, copy.deepcopy(Map)))

print(safe)