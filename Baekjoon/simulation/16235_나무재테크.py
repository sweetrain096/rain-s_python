import sys
import pprint
sys.stdin = open("16235_input.txt")

N, M, K = map(int, input().split())
A = []
for r in range(N):
    A.append(list(map(int, input().split())))
# pprint.pprint(A)

def is_wall(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    return False

Tree_map = []
for cnt in range(M):
    x, y, z = map(int, input().split())
    Tree_map.append([z, x-1, y-1])
Tree_map.sort(reverse=True)
fertilize = [[5 for _ in range(N)] for _ in range(N)]
# print(fertilize)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(K):
    for season in range(4):
        # 봄
        if season == 0:
            for j in range(len(Tree_map)-1, -1, -1):
                z, x, y = Tree_map[j]
                if fertilize[x][y] - z < 0:
                    Tree_map[j][0] = -Tree_map[j][0]
                else:
                    fertilize[x][y] -= z
                    Tree_map[j][0] += 1
            Tree_map.sort(reverse=True)
        # 여름
        elif season == 1:
            for j in range(len(Tree_map)-1, -1, -1):
                z, x, y = Tree_map[j]
                if z < 0:
                    fertilize[x][y] += int((-z)/2)
                    Tree_map.pop()
                else:
                    break
        # 가을
        elif season == 2:
            for j in range(len(Tree_map)):
                z, x, y = Tree_map[j]
                if not z % 5:
                    for iter_cnt in range(8):
                        px, py = dx[iter_cnt], dy[iter_cnt]
                        nx, ny = x + px, y + py
                        if not is_wall(nx, ny):
                            Tree_map.append([1, nx, ny])
            Tree_map.sort(reverse=True)
        # 겨울
        else:
            for r in range(N):
                for c in range(N):
                    fertilize[r][c] += A[r][c]

print(len(Tree_map))

