import sys
sys.stdin = open("sample2_input.txt")

for t in range(int(input())):
    a = [i for i in range(1, 13)]
    length = len(a)
    n, k = list(map(int, input().split()))
    result = 0
    for i in range(1 << length) :
        subset_a = []
        check = 0
        for j in range(length):
            if i & (1 << j) :
                subset_a.append(a[j])
        if len(subset_a) == n:
            # print(subset_a)
            for item_a in subset_a:
                check += item_a
                # print(item_a, end=" ")
            if check == k :
                result += 1

    print(f"#{t + 1} {result}")