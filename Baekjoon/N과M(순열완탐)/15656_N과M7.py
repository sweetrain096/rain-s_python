import sys
sys.stdin = open("15656_input.txt")


def permutation(r, result):
    if not r:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        result.append(arr[i])
        permutation(r-1, result)
        result.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
permutation(m, [])