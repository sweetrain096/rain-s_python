import sys
sys.stdin = open("2761_input.txt")

def bfs(a, b, n, m):
    Q = []
    if n - 1 >= 0:
        Q.append(n - 1)
    if n + 1 <= 100000:
        Q.append(n + 1)
    if n * a <= 100000:
        Q.append(n + a)
        Q.append(n * a)
    if n * b <= 100000:
        Q.append(n + b)
        Q.append(n * b)


a, b, n, m = map(int, input().split())
visited = []