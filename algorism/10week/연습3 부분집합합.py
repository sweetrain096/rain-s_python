'''
아래의 10개의 정수 집합에 대한 모든 부분집합 중
원소의 합이 10이 되는 부분집합을 모두 출력하시오.
ex) {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
'''

def powerset(n, k, sum_data):
    global total
    total += 1
    if sum_data == sum_check:
        for i in range(k):
            if tmp[i]:
                print(data[i], end=" ")
            else:
                print(" ", end = " ")
        print()
        return
    elif sum_data > sum_check:
        return

    if n == k:
        return

    else:
        tmp[k] = 1

        powerset(n, k + 1, sum_data + data[k])
        tmp[k] = 0
        powerset(n, k + 1, sum_data)

total = 0
n = 10
sum_check = 10
data = [i for i in range(1, 11)]
tmp = [0] * n
powerset(n, 0, 0)
print("호출 횟수 : ", total)