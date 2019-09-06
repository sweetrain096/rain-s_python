import sys
import pprint
sys.stdin = open("16235_input.txt")

N, M, K = map(int, input().split())
A = []
for r in range(N):
    A.append(list(map(int, input().split())))
# pprint.pprint(A)

Tree_map = []
for cnt in range(M):
    x, y, z = map(int, input().split())
    Tree_map.append([z, y-1, x-1])
Tree_map.sort(reverse=True)
print(Tree_map)
fertilize = [[5 for _ in range(N)] for _ in range(N)]
# print(fertilize)
for i in range(K):
    for season in range(4):
        # 봄
        if season == 0:
            for j in range(len(Tree_map)-1, -1, -1):
                print(Tree_map[j])
                z, y, x = Tree_map[j]
                fertilize[y][x] -= z
                if fertilize[y][z] < 0:
                    Tree_map[j][0] = -1
                else:
                    Tree_map[j][0] += 1
        # 여름
        elif season == 1:
            for j in range(len(Tree_map))

            print(Tree_map)

