import sys
sys.stdin = open("2583_input.txt")
# 재귀 깊이가 깊어지면 런타임에러가 나기 때문에 설정.
sys.setrecursionlimit(100000)

def iswall(row, col):
    if row < 0 or row >= m or col < 0 or col >= n:
        return True

def dfs(row, col):
    global cnt
    base[row][col] = 1
    cnt += 1
    for r, c in deg:
        pr, pc = row + r, col + c
        if not iswall(pr, pc) and not base[pr][pc]:
            dfs(pr, pc)
    return


m, n, k = map(int, input().split())
base = [[0 for _ in range(n)] for _ in range(m)]
deg = [[0, -1], [-1, 0], [0, 1], [1, 0]]
for i in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    for row in range(r1, r2):
        for col in range(c1, c2):
            base[row][col] = 1

result = []
for row in range(m):
    for col in range(n):
        cnt = 0
        if not base[row][col]:
            dfs(row, col)
            result.append(cnt)

print(len(result))
print(' '.join(map(str, sorted(result))))