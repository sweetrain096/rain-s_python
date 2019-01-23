'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''

def is_wall(x, y):
    if x < 0 or x >= 5 :
        return True
    if y< 0 or y >= 5:
        return True
    return False

def cal_abs(x, y):
    if x - y >= 0 :
        return x - y
    else :
        return y - x
arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))

print(arr)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum_items = 0

for x in range(len(arr)):
    for y in range(len(arr[x])):

        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            # check = arr[testX][testY]
            # sum_items += cal_abs(arr[x][y], check)
            if not is_wall(testX, testY):
                sum_items += cal_abs(arr[y][x], arr[testY][testX])

        print("1",sum_items)