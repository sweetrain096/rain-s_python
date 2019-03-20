import sys
sys.stdin = open("1991_input.txt")

def pre(node):
    if node:
        result.append(chr(node + 64))
        pre(tree[node][1])
        pre(tree[node][2])

def inorder(node):
    if node:
        inorder(tree[node][1])
        result.append(chr(node + 64))
        inorder(tree[node][2])

def post(node):
    if node:
        post(tree[node][1])
        post(tree[node][2])
        result.append(chr(node + 64))

n = int(input())
tree = [[0, 0, 0]]

for i in range(n):
    tmp = []
    for j in input().split():
        if j == '.':
            tmp.append(0)
        else:
            tmp.append(ord(j)-64)
    tree.append(tmp)
tree.sort()

result = []
pre(1)
print(''.join(result))
result = []
inorder(1)
print(''.join(result))
result = []
post(1)
print(''.join(result))