import sys
sys.stdin = open("15649_input.txt")
import time
start_time = time.time()


def permutation(pos, arr, visited):
    visited[pos] = 1
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if visited[i]:
           continue
        arr.append(i)
        visited[i] = 1
        permutation(i, arr, visited)
        arr.pop()
        visited[i] = 0

n, m = map(int, input().split())

for start in range(1, n+1):
    permutation(start, [start], [0 for _ in range(n+1)])

print(time.time() - start_time)