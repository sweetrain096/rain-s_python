'''
첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개
간선이 나열된다. 간선은 그것을 이루는 두 정점으로 표기된다. 간선은
항상 '부모 자식' 순서로 표기된다. 아래 예에서 두 번째 줄 처음
1과 2는 정점 1과 2를 잇는 간선을 의미하며, 1이 부모, 2가 자식을
의미한다. 간선은 부모 정점 번호가 작은것부터 나열되고,
부모 정점이 동일하다면 자식 정점 번호가 작은 것 부터 나열된다.

이진 트리의 표현에 대하여 전위 순회 정점의 번호를 출력하라.
13 : 정점의 개수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
total = 13
input_list = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
data = list(map(int, input_list.split()))
tree = [[0 for _ in range(4)] for _ in range(total)]
print(len(data))
for i in range(total):
    tree[i][0] = i + 1
for i in range(len(data) // 2):
    tree[i][0] = i + 1
    if not tree[data[i * 2] - 1][1]:
        tree[data[i * 2] - 1][1] = data[i * 2 + 1]
    else:
        tree[data[i * 2] - 1][2] = data[i * 2 + 1]
    if not tree[data[i * 2 + 1] - 1][3]:
        tree[data[i * 2 + 1] - 1][3] = data[i * 2]

for j in tree:
    print("%2d %2d %2d %2d" % (j[0], j[1], j[2], j[3]))
    if j[-1] == 0:
        start = j[0]


pre_result =[]
def pre_traver(node):
    if node != 0:
        pre_result.append(node)
        pre_traver(tree[node - 1][1])
        pre_traver(tree[node - 1][2])

pre_traver(1)
print(pre_result)


inorder_result = []
def inorder_traversal(node):
    if node != 0:
        inorder_traversal(tree[node - 1][1])
        inorder_result.append(node)
        inorder_traversal(tree[node - 1][2])
inorder_traversal(1)
print(inorder_result)

post_result = []
def post_traversal(node):
    if node != 0:
        post_traversal(tree[node - 1][1])
        post_traversal(tree[node - 1][2])
        post_result.append(node)
post_traversal(1)
print(post_result)



