'''
10개의 정수를 입력받아 부분집합의 합이 0이 되는 부분집합이 몇개인지
계산하는 함수를 작성해보자
'''

arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)

check_cnt = 0

for i in range (1, 1 << n):
    arr_sum = 0
    for j in range(n):
        if i & (1 << j):
            arr_sum += arr[j]
            print(arr[j], end = " ")

    if not arr_sum :
        check_cnt += 1
    print()
print(check_cnt)