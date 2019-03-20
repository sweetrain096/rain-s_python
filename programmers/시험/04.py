'''
10
8
4
7
8
10
2
9
7
8
12
'''

result = 0
check = 0
for n in range(int(input())):
    now = int(input())
    if not check:
        check = now
        tmp = 0
    if check <= now:
        result = max(result, tmp + 1)
        tmp = 0
        check = now
    else:
        tmp += 1

print(result)