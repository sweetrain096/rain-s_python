import sys
sys.stdin = open("1231_input.txt")

def inorder(node):
    global result
    if node:
        inorder(tree[node[1]])
        result += node[0]
        inorder(tree[node[2]])


for tc in range(10):
    n = int(input())
    tree = [[]]
    result = ""
    for i in range(n):
        tmp = input().split()
        insert_data = [tmp[1]]
        for j in range(2, len(tmp)):
            insert_data.append(int(tmp[j]))
        if len(insert_data) == 1:
            insert_data.extend([0, 0])
        elif len(insert_data) == 2:
            insert_data.append(0)
        tree.append(insert_data)
    inorder(tree[1])
    print(f"#{tc + 1} {result}")