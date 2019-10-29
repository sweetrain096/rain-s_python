import sys
sys.stdin = open("2_input.txt")

def perm(n, j):
    if n == j:
        perm_list.append(int(''.join(a)))
    else:
        for i in range(j, n):
            a[i], a[j] = a[j], a[i]
            perm(n, j + 1)
            a[i], a[j] = a[j], a[i]



a = input().split()
n = len(a)
k = int(input())
perm_list = []

perm(n, 0)
perm_list.sort()
if perm_list[k-1] <10**(n-1):
    print("0"+str(perm_list[k-1]))
else:
    print(perm_list[k-1])