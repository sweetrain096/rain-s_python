import sys
sys.stdin = open("5249_input.txt")


def MST_PRIM():
    s = 0
    key[s] = 0  # 시작 정점 가중치 = 0
    weight = 0
    min_idx = s

    # 정점의 개수 만큼 반복
    for _ in range(N):
        Min = 999999999
        # 방문 안 한 정점 중 최소 가중치 정점 찾기
        for i in range(N):
            if not visited[i] and key[i] < Min:
                Min = key[i]
                min_idx = i

        visited[min_idx] = 1
        weight += key[min_idx]

        for i in range(N):
            # if G[min_idx][i] 조건 필수. 0이라면 그래프 연결이 안 된것.
            if G[min_idx][i] and not visited[i] and G[min_idx][i] < key[i]:
                key[i] = G[min_idx][i]
                pi[i] = min_idx
        # print(weight, min_idx)
        # print(key)
        # print(pi)
    return weight

for tc in range(int(input())):
    V, E = map(int, input().split())
    N = V + 1
    G = [[0 for _ in range(N)] for _ in range(N)]

    key = [999999999 for _ in range(N)] # 그래프에 속한 정점의 가중치 저장 리스트
    pi = [-1 for _ in range(N)] # 트리에 연결될 부모 정점 저장 리스트.
    visited = [0 for _ in range(N)] # 방문 체크 리스트

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w
        G[n2][n1] = w


    print(f"#{tc + 1} {MST_PRIM()}")