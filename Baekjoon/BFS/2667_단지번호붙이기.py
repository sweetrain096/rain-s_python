import sys
sys.stdin = open("2667_input.txt")

def iswall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().strip())))

Q = []
total = 0
result = []
for row in range(n):
    for col in range(n):
        if data[row][col]:
            Q.append([row, col])
            while Q:
                r, c = Q.pop(0)
                if not iswall(r + 1, c) and data[r + 1][c]:
                    Q.append([r + 1, c])
                    data[r + 1][c] = 0
                    total += 1
                if not iswall(r - 1, c) and data[r - 1][c]:
                    Q.append([r - 1, c])
                    data[r - 1][c] = 0
                    total += 1
                if not iswall(r, c + 1) and data[r][c + 1]:
                    Q.append([r, c + 1])
                    data[r][c + 1] = 0
                    total += 1
                if not iswall(r, c - 1) and data[r][c - 1]:
                    Q.append([r, c - 1])
                    data[r][c - 1] = 0
                    total += 1
            result.append(total)
            total = 0
result.sort()
print(len(result))
for i in result:
    print(i)
