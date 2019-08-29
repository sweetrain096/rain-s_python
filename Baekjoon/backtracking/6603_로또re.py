import sys
sys.stdin = open("6603_input.txt")

def DFS(node):
    num = data[node]
    visit[num] = 1
    result.append(num)
    if len(result) == 6:
        print(' '.join(map(str, result)))
    for i in range(node + 1, k):
        if not visit[data[i]]:
            DFS(i)

    visit[num] = 0
    result.pop()

while True:
    data = list(map(int, input().split()))
    if data == [0]:
        break
    k = data.pop(0)
    result = []
    visit = [0] * 50
    for start in range(k-6 + 1):
        DFS(start)
    print()