import sys
sys.stdin = open("view_input.txt")
T = 10
for test_case in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    check = 0
    for i in range(2, len(data)-2) :
        max_floor = 0
        second_floor = 0
        for j in range(5) :
            if max_floor < data[i-2+j] :
                max_floor = data[i - 2 + j]
            elif max_floor == data[i-2+j]:
                max_floor = 0

        for j in range(5) :
            if second_floor < data[i-2+j] and data[i - 2 + j] != data[i] and data[i - 2 + j] != max_floor:
                second_floor = data[i - 2 + j]
        if data[i] == max_floor :

            check += max_floor - second_floor

    print(f"#{test_case+1} {check}")