import sys
sys.stdin = open("2468_input.txt")



deg = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Q = []
def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False

def bfs(rain):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(n):
            if Map[r][c] > rain and not visited[r][c]:
                cnt += 1
                Q.append([r, c])
                visited[r][c] = 1
                while Q:
                    tr, tc = Q.pop(0)
                    for dr, dc in deg:
                        nr = tr + dr
                        nc = tc + dc
                        if not is_wall(nr, nc) and not visited[nr][nc] and Map[nr][nc] > rain:
                            Q.append([nr, nc])
                            visited[nr][nc] = 1

    return cnt



n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
final = 1
for line in Map:
    final = max(final, max(line))
safe = 1

for rain in range(1, final+1):
    safe = max(safe, bfs(rain))

print(safe)