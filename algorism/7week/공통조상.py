import sys
sys.stdin = open("공통조상.txt")

def find(node, node_list):
    if tree[node][2]:
        node_list.append(tree[node][2])
        find(tree[node][2], node_list)
def correct(find1, find2):
    for i in find1:
        for j in find2:
            if i == j:
                return i

for tc in range(int(input())):
    v, e, node1, node2 = map(int, input().split())
    data = list(map(int, input().split()))
    # 트리만들기
    tree = [[0 for _ in range(3)] for _ in range(v + 1)]
    for i in range(e):
        if not tree[data[i * 2]][0]:
            tree[data[i * 2]][0] = data[i * 2 + 1]
        else:
            tree[data[i * 2]][1] = data[i * 2 + 1]

        if not tree[data[i * 2 + 1]][2]:
            tree[data[i * 2 + 1]][2] = data[i * 2]
    #
    # for i in tree:
    #     print(i)

    # 각각의 조상 찾기
    find1, find2 = [], []
    find(node1, find1)
    find(node2, find2)

    # 공통 조상 찾기
    if len(find1) > len(find2):
        result = correct(find1, find2)
    else:
        result = correct(find2, find1)
    # print(result)

    # 조상의 크기 찾기
    cnt = 1
    Q = [result]
    while Q:
        t = Q.pop(0)
        if tree[t][0]:
            Q.append(tree[t][0])
            cnt += 1
        if tree[t][1]:
            Q.append(tree[t][1])
            cnt += 1
    # print(cnt)


    print("#{} {} {}".format(tc + 1, result, cnt))