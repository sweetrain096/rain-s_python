import sys
sys.stdin = open("2817_input.txt")

for test_case in range(int(input())):
    n, k = list(map(int, input().split()))
    list_a = list(map(int, input().split()))
    lists = []
    check = 0
    for i in range(1 << n):
        lists = []
        for j in range(n):
            if i & (1 << j):
                lists.append(list_a[j])
        if sum(lists) == k :
            check += 1

    print(f"#{test_case + 1} {check}")