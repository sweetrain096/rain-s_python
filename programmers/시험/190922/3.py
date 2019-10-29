import sys
sys.stdin = open("3_input.txt")

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()

visit = [-1]
for i in data:
    start, end = i
    flag = False
    for j in range(len(visit)):
        if visit[j] <= start:
            visit[j] = end
            flag = True
            break
    if not flag:
        visit.append(end)

print(len(visit))