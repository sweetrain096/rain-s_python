import sys
sys.stdin = open("15651_input.txt")


def permutation(n, r, result):
    if not r:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n + 1):
        result.append(i)
        permutation(n, r-1, result)
        result.pop()


n, m = map(int, input().split())
permutation(n, m, [])