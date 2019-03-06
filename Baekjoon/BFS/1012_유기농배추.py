import sys
sys.stdin = open("1012_input.txt")

def iswall(r, c):
    if r < 0 or r >= height or c < 0 or c >= width:
        return True


for tc in range(int(input())):
    width, height, k = map(int, input().split())
    data = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1

    Q = []
    result = 0
    for row in range(height):
        for col in range(width):

            if data[row][col]:
                Q.append([row, col])
                result += 1
                # for i in data:
                #     print(i)
                # print()

                while Q:
                    t = Q.pop(0)
                    if not iswall(t[0] - 1, t[1]) and data[t[0] - 1][t[1]]:
                        Q.append([t[0] - 1, t[1]])
                        data[t[0] - 1][t[1]] = 0
                    if not iswall(t[0] + 1, t[1]) and data[t[0] + 1][t[1]]:
                        Q.append([t[0] + 1, t[1]])
                        data[t[0] + 1][t[1]] = 0
                    if not iswall(t[0], t[1] - 1) and data[t[0]][t[1] - 1]:
                        Q.append([t[0], t[1] - 1])
                        data[t[0]][t[1] - 1] = 0
                    if not iswall(t[0], t[1] + 1) and data[t[0]][t[1] + 1]:
                        Q.append([t[0], t[1] + 1])
                        data[t[0]][t[1] + 1] = 0


    print(result)

    # for i in data:
    #     print(i)
    # print()