import sys
sys.stdin = open("노드의합_input.txt")

def post_traversal(node):
    if node <= n and not tree[node]:
        post_traversal(node * 2)
        post_traversal(node * 2 + 1)
        if node * 2 <= n:
            if node * 2 + 1 <= n:
                tree[node] = tree[node * 2] + tree[node * 2 + 1]
            else:
                tree[node] = tree[node * 2]

for tc in range(int(input())):
    n, m, l = map(int, input().split())
    tree = [0 for i in range(n + 1)]
    for i in range(m):
        leaf, num = map(int, input().split())
        tree[leaf] = num
    post_traversal(l)

    print("#{} {}".format(tc + 1, tree[l]))