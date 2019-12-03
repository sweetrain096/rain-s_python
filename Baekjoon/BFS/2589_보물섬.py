import sys
sys.stdin = open("2589_input.txt")

deg = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    for nr in range(r):
        for nc in range(c):
            if Map[nr][nc] == 'L':

    return

r, c = map(int, input().split())
Map = []
for i in range(r):
    tmp = input()
    tmp_list = []
    for j in tmp:
        tmp_list.append(j)
    Map.append(tmp_list)

