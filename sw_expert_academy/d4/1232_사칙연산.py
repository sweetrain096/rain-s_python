import sys
sys.stdin = open("1232_input.txt")


def inorder(node):
    if node:
        inorder(tree[node][2])
        formula.append(tree[node][1])
        inorder(tree[node][3])

def calculate(formula):
    calc = formula[0]
    for i in range(int(len(formula)/2)):
        if formula[i * 2 + 1] == '-':
            calc -= formula[i * 2 + 2]
        elif formula[i*2+1] == '+':
            calc += formula[i*2+2]
        elif formula[i*2+1] == '*':
            calc *= formula[i*2+2]
        elif formula[i*2+1] == '/':
            calc /= formula[i*2+2]
    return calc

for tc in range(10):
    n = int(input())
    tree = [[0, 0, 0, 0]]
    for node in range(n):
        tmp = list(input().split())
        tmp[0] = int(tmp[0])
        if (len(tmp)) == 4:
            tmp[2] = int(tmp[2])
            tmp[3] = int(tmp[3])
        else:
            tmp[1] = int(tmp[1])
            tmp.extend([0,0])
        tree.append(tmp)
    print(tree)
    formula = []
    inorder(1)
    print(formula)
    print(calculate(formula))
