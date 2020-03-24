board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    for col in moves:
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
        for row in range(n):
            if board[row][col-1]:
                stack.append(board[row][col-1])
                board[row][col-1] = 0
                break


    return answer


print(solution(board, moves))