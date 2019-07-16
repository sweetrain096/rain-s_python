import sys
sys.stdin = open("최소신장트리_input.txt")

def find_set(x):
    if x == p[x] : return x
    else : return find_set(p[x])

def make_mst():
    cnt = 0             # 간선 개수
    result = 0          # 가중치의 합

    i = 0                           # 간선 관리
    while cnt < node_total:         # 트리에서 간선 개수는 노드 - 1
        p1 = find_set(graph[i][0])  # 가중치가 가장 작은 노드(순차적으로 내려간다.)의
        p2 = find_set(graph[i][1])  # 두 노드의 대표 원소를 p1, p2에서 찾는다.
        if p1 != p2:
            result += graph[i][2]
            cnt += 1
            p[p2] = p1              # 대표 원소를 하나로 합친다.
        i += 1                      # 다음 간선으로 이동
    return result


for tc in range(int(input())):
    node_total, edge_total = map(int, input().split())

    graph = [list(map(int, input().split())) for i in range(edge_total)]
    graph.sort(key=lambda x : x[2])         # 가중치 기준 오름차순 정렬
    p = list(range(node_total + 1))         # make set. 대표 원소 초기화

    print(p)
    for i in graph:
        print(i)


    print("#{} {}".format(tc + 1, make_mst()))

