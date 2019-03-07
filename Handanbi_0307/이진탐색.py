import sys
sys.stdin = open("이진탐색_input.txt")

def inorder(node):
    global cnt, n
    if node:
        if node * 2 <= n:
            inorder(tree[node * 2][0])
        if not tree[node][1]:
            tree[node][1] = cnt
            cnt += 1
        if node * 2 + 1 <= n:
            inorder(tree[node * 2 + 1][0])


for tc in range(int(input())):
    n = int(input())
    tree = [[i, 0] for i in range(n + 1)]
    cnt = 1
    inorder(1)

    print("#{} {} {}".format(tc + 1, tree[1][1], tree[n // 2][1]))