import sys
sys.stdin = open("14502_input.txt")

from collections import deque

n, m = map(int, input().split())
data = []
bug = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            bug.append([i, j])
    data.append(tmp)

for i in data:
    print(i)
print(bug)