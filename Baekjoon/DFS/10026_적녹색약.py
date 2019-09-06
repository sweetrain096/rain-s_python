import sys
sys.stdin = open("10026_input.txt")

def is_wall(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False

def dfs(node):
    global cnt
    x, y = node[0], node[1]
    visit[x][y] = 1




    visit[x][y] = 0





data = []
cnt = 0
n = int(input())
visit = [[0 for i in range(n)] for j in range(n)]
result = []
for i in range(n):
    data.append(list(input()))

print(data)