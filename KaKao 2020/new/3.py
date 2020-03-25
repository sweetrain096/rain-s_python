def is_unlock(key, lock, r, c):
    new_lock = [[0 for _ in range(len(key) + len(lock) - 1)] for _ in range(len(key) + len(lock) - 1)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[len(key) + i - 1][len(key) + j - 1] = lock[i][j]
    start = len(key) - 1
    end = len(key) + len(lock) - 1
    for nr in range(len(key)):
        for nc in range(len(key)):
            # print(r, c, nr, nc, r+nr, c+nc)
            # print(key[nr][nc], new_lock[r+nr][c+nc])
            if not key[nr][nc]:
                continue
            if r+nr >= len(new_lock) or c+nc >= len(new_lock):
                continue
            if new_lock[r+nr][c+nc]:
                return False
            new_lock[r+nr][c+nc] = 1

    # for i in key:
    #     print(i)
    # print()
    # for i in new_lock:
    #     print(i)

    for i in range(start, end):
        for j in range(start, end):
            if not new_lock[i][j]:
                return False
    return True


def unlock(key, lock):
    for r in range(len(key) + len(lock) - 1):
        for c in range(len(key) + len(lock) - 1):
            if is_unlock(key, lock, r, c):
                return True
    return False


def solution(key, lock):
    answer = True
    new_key = [[0 for _ in range(len(key))] for _ in range(len(key))]
    for i in range(4):
        if not i:
            for j in range(len(key)):
                new_key[j][:] = key[j][:]
        elif i == 1:
            for r in range(len(key)):
                for c in range(len(key)):
                    new_key[c][len(key) - r - 1] = key[r][c]
        elif i == 2:
            for r in range(len(key)):
                for c in range(len(key)):
                    new_key[len(key) - r - 1][len(key) - c - 1]  = key[r][c]
        else:
            for r in range(len(key)):
                for c in range(len(key)):
                    new_key[len(key) - c - 1][r] = key[r][c]
        if unlock(new_key, lock):
            return answer

    answer = False
    return answer



key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# key = [[0, 1, 0], [0, 1, 1], [1, 1, 0]]
# lock = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print(solution(key, lock))