import sys
sys.stdin = open("1974_input.txt")

def check():
    for i in range(9):
        check_row = [0 for _ in range(10)]
        check_col = [0 for _ in range(10)]
        for j in range(9):
            check_row[sudoku[i][j]] += 1
            check_col[sudoku[j][i]] += 1
        if 0 in check_row[1:]:
            return 0
        if 0 in check_col[1:]:
            return 0
    for row in range(3):
        for col in range(3):
            check_box = [0 for _ in range(10)]
            for plus in range(3):
                check_box[sudoku[row * 3 + plus][col * 3]] += 1
                check_box[sudoku[row * 3 + plus][col * 3 + 1]] += 1
                check_box[sudoku[row * 3 + plus][col * 3 + 2]] += 1
            if 0 in check_box[1:]:
                return 0
    return 1

for tc in range(int(input())):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))
    print("#{} {}".format(tc + 1, check()))