'''
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''

def is_wall(x, y, check):
    print(x, y)
    if x < 0 or x >= 5 :
        return True
    elif y < 0 or y >= 5 :
        return True
    elif check == 0 and arr[x][y] != 0:
        return True
    elif check == 1 and arr[x][y] != 0 :
        return True
    elif check == 2 and arr[x][y] != 0 :
        return True
    elif check == 3 and arr[x][y] != 0 :
        return True

    return False


def selection_sort(a, b):

    for i in range(24):
        min_x = i // 5
        min_y = i % 5
        for j in range(i + 1, 25):
            if a[min_x][min_y] > a[j // 5][j % 5]:
                min_x, min_y = j // 5, j % 5
        a[i // 5][i % 5], a[min_x][min_y] = a[min_x][min_y], a[i // 5][i % 5]


    # min_x, min_y = 0, 0
    # for i in range(24):
    #     # min_x = i // 5
    #     # min_y = i % 5
    #     if a[i // 5][i % 5]
    #     for j in range(i + 1, 25):
    #         if a[min_x][min_y] > a[j // 5][j % 5]:
    #             min_x, min_y = j // 5, j % 5
    #     a[i // 5][i % 5], a[min_x][min_y] = a[min_x][min_y], a[i // 5][i % 5]




    check = 0
    x = 0
    y = 0
    for i in range(25):
        #print(x, y)
        #print(check)
        if check % 4 == 0:
            b[x][y] = a[i // 5][i % 5]
            y += 1
            if is_wall(x, y, check):
                y -= 1
                check += 1

        elif check % 4 == 1 :
            b[x][y] = a[i // 5][i % 5]
            x += 1
            if is_wall(x, y, check):
                x -= 1
                check += 1
        elif check % 4 == 2:
            b[x][y] = a[i // 5][i % 5]
            y -= 1
            if is_wall(x, y, check):
                y += 1
                check += 1
        else :
            b[x][y] = a[i // 5][i % 5]
            x -= 1
            if is_wall(x, y, check):
                x += 1
                check += 1





arr = [[0 for _ in range(5)] for _ in range(5)]
#
# check_arr = [[0 for _ in range(5)] for _ in range(5)]
# for i in range(5):
#     check_arr[i] = list(map(int, input().split()))


check_arr = [[9, 20, 2, 18, 11],
[19, 1, 25, 3, 21],
[8, 24, 10, 17, 7],
[15, 4, 16, 5, 6],
[12, 13, 22, 23, 14]]
selection_sort(check_arr, arr)

print(check_arr)
print(len(check_arr))

print(arr)