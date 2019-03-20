import sys
sys.stdin = open("1967_input.txt")



n = int(sys.stdin.readline())
tree = [[0, 0] for _ in range(n + 1)]
weight = [[0, 0] for _ in range(n + 1)]
while True:
    tmp = sys.stdin.readline()
    if not tmp:
        break
    tmp = list(map(int, tmp.split()))

    print(tmp)
    if not tree[tmp[0]][0]:
        tree[tmp[0]][0] = tmp[1]
        weight[tmp[0]][0] = tmp[2]
    else:
        tree[tmp[0]][1] = tmp[1]
        weight[tmp[0]][1] = tmp[2]

print(tree)
print(weight)