import sys
sys.stdin = open("15656_input.txt")


def combination(pos, r, result):
    if not r:
        print(' '.join(map(str, result)))
        return
    if not pos:
        return
    result.append(data[pos-1])
    combination(pos, r-1, result)
    result.pop()
    combination(pos-1, r, result)
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
combination(n, m, [])
