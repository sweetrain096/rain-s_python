import sys
sys.stdin = open("5188_input.txt")

def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True

def find(r, c, sum_data):
    global result

    if sum_data > result:
        return
    if r == c and r == n - 1:
        result = min(result, sum_data)
        return
    else:
        for dr, dc in deg:
            nr, nc = dr + r, dc + c
            if not is_wall(nr, nc):
                find(nr, nc, sum_data + data[nr][nc])


deg = ((1, 0), (0, 1))

for tc in range(int(input())):
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    result = 999999999999
    find(0, 0, data[0][0])



    print("#{} {}".format(tc + 1, result))