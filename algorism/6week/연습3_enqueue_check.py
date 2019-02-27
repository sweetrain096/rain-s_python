'''
다음은 연결되어있는 두 개의 정점 사이의 간선을
순서대로 나열해 놓은 것.
모든 정점을 너비우선탐색하여 경로를 출력하시오
시작정점을 1로 시작하시오
정점 : 7개 간선 : 8개
1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
출력 결과의 예는 다음과 같다.
1-2-3-4-5-7-6
'''


def BFS(g, start):
    global v
    visited = [0] * (v + 1)

    # Q에 첫번째 넣을때에는 무조건 방문 안했으니까
    # visited check
    Q = []
    Q.append(start)
    visited[start] = 1
    print(start)
    # 방문 했을때 프린트
    while Q:
        t = Q.pop(0)

        for w in range(1, v + 1):
            if g[t][w] and not visited[w]:
                Q.append(w)
                visited[w] = 1
                print(w)
                # 방문 했을 때 프린트






    return

v, e = 7, 8
data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
g = [[0 for _ in range(v + 1)] for _ in range(v + 1)]



start = 1

for i in range(e):
    g[data[i * 2]][data[i * 2 + 1]] = 1
    g[data[i * 2 + 1]][data[i * 2]] = 1

BFS(g, start)


for i in range(1, v + 1):
    for j in range(1, v + 1):
        print(g[i][j], end=" ")
    print()