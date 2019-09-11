import sys
sys.stdin = open("9663_input.txt")

def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False

def visit_check(nr, nc):
    for i in range(n):
        Map[nr][i] += 1
        Map[i][nc] += 1
        if not is_wall(nr + i + 1, nc + i + 1):
            Map[nr + i + 1][nc + i + 1] += 1
        if not is_wall(nr - i - 1, nc - i - 1):
            Map[nr - i - 1][nc - i - 1] += 1
        if not is_wall(nr + i + 1, nc - i - 1):
            Map[nr + i + 1][nc - i - 1] += 1
        if not is_wall(nr - i - 1, nc + i + 1):
            Map[nr - i - 1][nc + i + 1] += 1

def visit_uncheck(nr, nc):
    for i in range(n):
        Map[nr][i] -= 1
        Map[i][nc] -= 1
        if not is_wall(nr + i + 1, nc + i + 1):
            Map[nr + i + 1][nc + i + 1] -= 1
        if not is_wall(nr - i - 1, nc - i - 1):
            Map[nr - i - 1][nc - i - 1] -= 1
        if not is_wall(nr + i + 1, nc - i - 1):
            Map[nr + i + 1][nc - i - 1] -= 1
        if not is_wall(nr - i - 1, nc + i + 1):
            Map[nr - i - 1][nc + i + 1] -= 1

def backtracking(node):
    global cnt
    nr, nc = node

    if nr == n - 1:
        cnt += 1


    # visit 체크
    visit_check(nr, nc)
    for i in range(n):
        if not is_wall(nr + 1, i) and not Map[nr + 1][i]:
            backtracking([nr + 1, i])

    visit_uncheck(nr, nc)





n = int(input())
Map = [[0 for _ in range(n)] for _ in range(n)]


cnt = 0

for i in range(n):
    backtracking([0, i])

print(cnt)