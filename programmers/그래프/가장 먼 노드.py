import collections

Graph = dict()
visited = []


def bfs(n):
    result = []
    Q = collections.deque()
    Q.append([1, 0])
    visited[1] = 1
    while Q:
        t, cnt = Q.popleft()
        result.append((t, cnt))
        for i in Graph[t]:
            if not visited[i]:
                visited[i] = 1
                Q.append([i, cnt+1])
    return result
    # result = []
    # Q = [0 for _ in range(n * n * 2)]
    # rp = 0
    # wp = 0
    # Q[wp] = (1, 0)
    # wp += 1
    # visited[1] = 1
    # while rp < wp:
    #     t, cnt = Q[rp]
    #     rp += 1
    #     result.append((t, cnt))
    #     for i in Graph[t]:
    #         if not visited[i]:
    #             visited[i] = 1
    #             Q[wp] = (i, cnt+1)
    #             wp += 1
    # return result


def solution(n, edges):
    answer = 0
    for i in range(n+1):
        visited.append(0)
    for edge in edges:
        s, e = edge
        if Graph.get(s):
            Graph[s].append(e)
        else:
            Graph[s] = [e]
        if Graph.get(e):
            Graph[e].append(s)
        else:
            Graph[e] = [s]



    bfs_data = bfs(n)
    Max = bfs_data[-1][1]
    # print(bfs_data)
    for i in range(len(bfs_data)-1, -1, -1):
        if bfs_data[i][1] == Max:
            answer += 1
    return answer


vvv = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
nnn = 6

print(solution(nnn, vvv))