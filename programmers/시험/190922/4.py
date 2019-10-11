import sys
sys.stdin = open("4_input.txt")

n = int(input())
data = list(map(int, input().split()))
abs_list = [0 for _ in range(n)]

for i in range(n):
    if data[i]:
        continue
    # left
    l_cnt = 0
    if i != 0:
        for j in range(i-1, -1, -1):
            l_cnt += 1
            if data[j]:
                break

    # right
    r_cnt = 0
    if i != n-1:
        for j in range(i+1, n):
            r_cnt += 1
            if data[j]:
                break
    if not l_cnt:
        abs_list[i] = r_cnt
    elif not r_cnt:
        abs_list[i] = l_cnt
    else:
        abs_list[i] = min(l_cnt, r_cnt)
print(max(abs_list))