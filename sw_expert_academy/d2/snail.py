import sys
sys.stdin = open("snail_input.txt")

def is_wall(row, col):
    if col < 0 or col >= n or row < 0 or row >= n:
        return True
    elif snail_list[row][col]:
        return True
    return False


for test_case in range(int(input())):
    n = int(input())
    snail_list = [[0 for i in range(n)] for j in range(n)]
    direction = 0
    row, col = 0, 0

    for plus in range(n*n):
        snail_list[row][col] = plus + 1

        if not direction % 4:
            col += 1
            if is_wall(row, col):
                col -= 1
                row += 1
                direction += 1
        elif direction % 4 == 1 :
            row += 1
            if is_wall(row, col):
                row -= 1
                col -= 1
                direction += 1
        elif direction % 4 == 2:
            col -= 1
            if is_wall(row, col):
                col += 1
                row -= 1
                direction += 1
        else :
            row -= 1
            if is_wall(row, col):
                row += 1
                col += 1
                direction += 1




    print(f"#{test_case + 1}")
    for cnt in range(n):
        print(f"{' '.join(map(str,snail_list[cnt]))}")