check_arr = [[9, 20, 2, 18, 11],
[19, 1, 25, 3, 21],
[8, 24, 10, 17, 7],
[15, 4, 16, 5, 6],
[12, 13, 22, 23, 14]]

result_arr = [[0 for i in range(5)] for i in range(5)]

def select_min(check_list):
    min_check = check_list[0][0]
    for i in range(25):
        if min_check >= check_list[i // 5][i % 5]:
            min_check = check_list[i // 5][i % 5]
            min_y = i // 5
            min_x = i % 5
    check_list[min_y][min_x] = 30000
    return min_check

def is_wall(y, x, check):
    if y < 0 or y >= 5 :
        return True
    elif x < 0 or x >= 5:
        return True
    elif result_arr[y][x] != 0:
        return True
    return False

y, x = 0, 0
check = 1
for i in range (25):
    min_check = select_min(check_arr)
    print(y, x, check, min_check)

    result_arr[y][x] = min_check

    if check % 4 == 1:
        x += 1
        if is_wall(y, x, check):
            x -= 1
            check += 1
    if check % 4 == 2:
        y += 1
        if is_wall(y, x, check):
            y -=1
            check += 1
    if check % 4 == 3:
        x -= 1
        if is_wall(y, x, check):
            x += 1
            check += 1

    if check % 4 == 0 :
        y -= 1
        if is_wall(y, x, check):
            y += 1
            x += 1
            check += 1
print(result_arr)

