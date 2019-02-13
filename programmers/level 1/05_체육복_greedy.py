def solution(n, losts, reserves):
    answer = 0
    students = [1] * n
    for reserve in reserves:
        students[reserve - 1] += 1
    for lost in losts:
        students[lost - 1] = 0

    print(students)





    return answer










result = solution(5, [2, 4], [1, 3, 5])
print(result)

result = solution(5, [2, 4], [3])
print(result)