import sys
sys.stdin = open("1697_input.txt")

def BFS(n, k):
    Q = []
    Q.append(n)
    visited[n] = 1
    check = Q[-1]
    depth = 0
    while Q:
        t = Q.pop(0)
        if t == k:
            return depth
        # print(2 * k, t - 1)
        if t - 1 >= 0 and t - 1 < 100001 and not visited[t - 1]:
            visited[t - 1] = 1
            Q.append(t - 1)
        if t + 1 < 100001 and not visited[t + 1]:
            visited[t + 1] = 1
            Q.append(t + 1)
        if 2 * t < 100001 and not visited[2 * t]:
            visited[2 * t] = 1
            Q.append(2 * t)

        if t == check:
            depth += 1
            check = Q[-1]
    return 0


n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
print(BFS(n, k))