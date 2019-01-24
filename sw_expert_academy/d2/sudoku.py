import sys
sys.stdin = open("sudoku_input.txt")

for test_case in range(int(input())):
    puzzle = []
    check = {i for i in range(1, 10)}
    answer = 1
    for i in range(9):
        # row
        puzzle.append(list(map(int, input().split())))
        if check - set(puzzle[i]):
            answer = 0

    if answer:
        # col
        for row in range(9):
            check = {i for i in range(1, 10)}
            for col in range(9):
                check = check - set([puzzle[col][row]])
            if check :
                answer = 0
                break
    if answer:

        # square
        for row in range(3):
            for col in range(3):
                check = {i for i in range(1, 10)}
                check -= set(puzzle[row * 3 + 0][col * 3 : col * 3 + 3])
                check -= set(puzzle[row * 3 + 1][col * 3 : col * 3 + 3])
                check -= set(puzzle[row * 3 + 2][col * 3 : col * 3 + 3])
                if check :
                    answer = 0
                    break


    print(f"#{test_case + 1} {answer}")