import sys
sys.stdin = open("사칙연산_input.txt")

def postorder(node):
    global result
    if node:
        if tree[node][0] in operator:
            postorder(tree[node][1])
            postorder(tree[node][2])
            left, right = tree[node][1], tree[node][2]
            if tree[node][0] == "+":
                tree[node][0] = tree[left][0] + tree[right][0]
            elif tree[node][0] == "-":
                tree[node][0] = tree[left][0] - tree[right][0]
            elif tree[node][0] == "/":
                tree[node][0] = tree[left][0] / tree[right][0]
            elif tree[node][0] == "*":
                tree[node][0] = tree[left][0] * tree[right][0]
            # print("result", tree[node][1],  tree[node][2], tree[node][0])
    return tree[node][0]

operator = ["+", "-", "*", "/"]

for tc in range(10):
    n = int(input())
    tree = [[0 for _ in range(3)] for _ in range(n + 1)]
    for i in range(n):
        data = list(input().split())
        # tree[int(data[0])][0] = int(data[0])
        if data[1] in operator:
            tree[int(data[0])][0] = data[1]
        else:
            tree[int(data[0])][0] = int(data[1])
        if len(data) > 2:
            tree[int(data[0])][1] = int(data[2])

            tree[int(data[0])][2] = int(data[3])

    result = 0

    print("#{} {}".format(tc + 1, int(postorder(1))))

