import sys
sys.stdin = open("1251_input.txt")

def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def MST_KRUSKAL():
    mst = []
    mst_cost = 0

    while len(mst) < n-1:
        u, v, val = G.pop()
        pu = find_set(u)
        pv = find_set(v)
        if pu != pv:
            mst.append((u, v))
            mst_cost += val
            p[pv] = pu  # union
    return mst_cost


for tc in range(int(input())):
    n = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    G = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            cost_x = X[i] - X[j]
            cost_y = Y[i] - Y[j]
            cost = cost_x * cost_x + cost_y * cost_y
            G.append([i, j, cost])
    G.sort(key=lambda k:k[2], reverse=True)
    p = list(range(n))  # 부모
    # print(G)

    result = round(MST_KRUSKAL()*E)
    print(f"#{tc + 1} {result}")