'''
10
5 10
0000000000
0123456789
0000000000
0000000000
0000000000
'''
T = int(input())
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
print(arr)
print(T)
print(n, m)

for i in range(0, n):
    for j in range(0, m):
        print(arr[i][j], end="")
    print()