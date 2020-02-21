import sys
sys.stdin = open("sample4_input.txt")

for t in range(int(input())):
    n = int(input())
    input_list = list(map(int, input().split()))

    cnt = 0
    for i in range(n- 1):
        cnt += 1
        min_check = i
        max_check = i
        for j in range(i + 1, n):
            if cnt % 2 :
                if input_list[max_check] < input_list[j]:
                    max_check = j
            else:
                if input_list[min_check] > input_list[j]:
                    min_check = j
        if cnt % 2 :
            input_list[i], input_list[max_check] = input_list[max_check], input_list[i]
        else:
            input_list[i], input_list[min_check] = input_list[min_check], input_list[i]


    print(f"#{t + 1} {' '.join(map(str,input_list[:10]))}")