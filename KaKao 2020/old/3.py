key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
import pprint


def rotation(key):
    results = [key]


    ro_data = key[:][:]
    for cnt in range(3):
        result = []
        for c in range(len(ro_data) - 1, -1, -1):
            tmp = []
            for r in range(len(ro_data)):
                tmp.append(ro_data[r][c])
            result.append(tmp)
        ro_data = result[:][:]
        results.append(result)
    return results



def solve(arr):
    return

def check(N, M, arr):
    for i in range(N):
        for j in range(N):
            if arr[i + M][j + M] != 1:
                return False
    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)

    answer = False
    board = [[0 for _ in range(N + 2 * M)] for _ in range(N + 2*M)]
    total = len(board)

    for i in range(N):
        for j in range(N):
            board[i + M][j + M] = lock[i][j]
    # pprint.pprint(board)


    candidates = rotation(key)

    for i in range(4):
        check_key = candidates[i]
        for r in range(total - M):
            for c in range(total - M):
                # 키 더하기
                for x in range(M):
                    for y in range(M):
                        board[r + x][c + y] += check_key[x][y]
                if check(N, M, board):
                    answer = True
                    return answer
                else:
                    for x in range(M):
                        for y in range(M):
                            board[r + x][c + y] -= check_key[x][y]


    return answer


print(solution(key, lock))