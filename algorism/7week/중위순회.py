import sys
sys.stdin = open("중위순회.txt")

def inorder(node):
    if node:
        inorder(tree[node][1])
        result.append(tree[node][0])
        inorder(tree[node][2])

for tc in range(10):
    n = int(input())
    tree = [[0 for _ in range(4)] for _ in range(n + 1)]
    for i in range(n):
        data = input().split()
        index = int(data[0])
        tree[index][0] = data[1]
        if len(data) >= 3:
            tree[index][1] = int(data[2])
            if not tree[int(data[2])][3]:
                tree[int(data[2])][3] = index
        if len(data) == 4:
            tree[index][2] = int(data[3])
            if not tree[int(data[3])][3]:
                tree[int(data[3])][3] = index

    # for i in tree:
    #     print(i)
    result = []
    inorder(1)
    print("#{} {}".format(tc + 1, ''.join(result)))