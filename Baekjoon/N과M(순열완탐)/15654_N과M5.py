import sys
sys.stdin = open("15654_input.txt")


def permutation(pos, visited, result):
    visited[pos] = 1
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        if visited[i]:
            continue
        result.append(data[i])
        visited[i] = 1
        permutation(i, visited, result)
        result.pop()
        visited[i] = 0

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

for start in range(n):
    permutation(start, [0 for _ in range(n+1)], [data[start]])
