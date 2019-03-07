import sys
sys.stdin = open("subtree_input.txt")

def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])




for tc in range(int(input())):
    e, root = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0 for _ in range(2)] for _ in range(e + 2)]

    for i in range(len(data) // 2):
        if not tree[data[i * 2]][0]:
            tree[data[i * 2]][0] = data[i * 2 + 1]
        elif not tree[data[i * 2]][1]:
            tree[data[i * 2]][1] = data[i * 2 + 1]

    cnt = 0
    preorder(root)
    print("#{} {}".format(tc + 1, cnt))

