import sys
sys.stdin = open("15652_input.txt")


def combination(pos, r, result):
    if not r:
        print(' '.join(map(str, result)))
        return
    if not pos:
        return
    result.append(arr[pos - 1])
    combination(pos, r-1, result)
    result.pop()
    combination(pos - 1, r, result)


n, m = map(int, input().split())
arr = [i for i in range(n, 0, -1)]
combination(n, m, [])