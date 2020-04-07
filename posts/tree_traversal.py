import sys
sys.stdin = open("tree_input.txt")

def preorder(node):
    if node:
        print(tree[node][1], end=" ")
        preorder(tree[node][2])
        preorder(tree[node][3])

def inorder(node):
    if node:
        inorder(tree[node][2])
        print(tree[node][1], end=" ")
        inorder(tree[node][3])

def postorder(node):
    if node:
        postorder(tree[node][2])
        postorder(tree[node][3])
        print(tree[node][1], end=" ")

n = int(input())
tree = [[0, 0, 0, 0]]
for i in range(n):
    data = list(input().split())
    temp = [0, 0, 0, 0]
    temp[0] = int(data[0])
    temp[1] = data[1]
    if len(data) == 3:
        temp[2] = int(data[2])
    elif len(data) == 4:
        temp[2] = int(data[2])
        temp[3] = int(data[3])
    tree.append(temp)
preorder(1)
print("     -> 전위 순회")
inorder(1)
print("     -> 중위 순회")
postorder(1)
print("     -> 후위 순회")