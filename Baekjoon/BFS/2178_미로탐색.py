import sys
sys.stdin = open("2178_input.txt")

def iswall(r, c):
    global n, m
    if r < 0 or r >= n or c < 0 or c >= m:
        return True

def BFS(n, m, row, col):
    Q = []
    Q.append([row, col])
    maze[row][col] = 0
    check = [row, col]
    depth = 1
    while Q:
        # print(Q)
        t = Q.pop(0)
        # print(Q, t, depth)
        if t == [n - 1, m - 1]:
            return depth
        for i in range(4):
            if not iswall(t[0] + deg[i][0], t[1] + deg[i][1]) and maze[t[0] + deg[i][0]][t[1] + deg[i][1]]:
                maze[t[0] + deg[i][0]][t[1] + deg[i][1]] = 0
                Q.append([t[0] + deg[i][0], t[1] + deg[i][1]])

        if check == t:
            depth += 1
            check = Q[-1]
        # for i in maze:
        #     print(i)
        # print()


n, m = map(int, input().split())
maze = []
for i in range(n):
    tmp = []
    for j in input():
        tmp.append(int(j))
    maze.append(tmp)
deg = [[0, -1], [1, 0], [0, 1], [-1, 0]]
row, col = 0, 0

print(BFS(n, m, 0, 0))


