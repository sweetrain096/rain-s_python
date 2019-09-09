import sys
sys.stdin = open("1233_input.txt")

def inorder(node):
    if node:
        inorder(tree[node][2])
        formula.append(tree[node][1])
        inorder(tree[node][3])


for tc in range(10):
    n = int(input())
    tree = [[0 for _ in range(4)] for _ in range(n+1)]
    for line in range(n):
        tmp = list(input().split())
        index = int(tmp[0])
        tree[index][0] = index
        if len(tmp)>=3:
            tree[index][2] = int(tmp[2])
        if len(tmp) == 4:
            tree[index][3] = int(tmp[3])
        # if tmp[1] in ['-', '+', '*', '/']:
        #     tree[index][1] = tmp[1]
        # else:
        #     tree[index][1] = int(tmp[1])
        tree[index][1] = tmp[1]
    formula = []
    inorder(1)
    result = 1
    for i in range(len(formula)):
        if not i%2:
            if ord(formula[i])<48 or ord(formula[i])>=58:
                result = 0
                break
        else:
            if formula[i] not in ['-', '+', '*', '/']:
                result = 0
                break
    print(f"#{tc + 1} {result}")
