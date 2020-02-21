import sys
sys.stdin = open("5249_input.txt")

def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def MST_KRUSKAL():
    mst = []

    mst_cost = 0
    while len(mst) < V:
        u, v, val = G.pop()
        pu = find_set(u)
        pv = find_set(v)
        if pu != pv:
            mst.append((u, v))
            mst_cost += val
            p[pv] = pu  # union
    return mst_cost


for tc in range(int(input())):
    V, E = map(int, input().split())
    N = V + 1

    G = [list(map(int, input().split())) for _ in range(E)]
    G.sort(key=lambda t:t[2], reverse=True)
    # make_set. 각 정점을 대표하는 상호배타 집합 생성
    p = list(range(N))



    print(f"#{tc + 1} {MST_KRUSKAL()}")