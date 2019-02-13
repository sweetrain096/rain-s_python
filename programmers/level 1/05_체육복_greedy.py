def solution(n, losts, reserves):
    answer = 0
    students = [1] * n
    for reserve in reserves:
        students[reserve - 1] += 1
    for lost in losts:
        students[lost - 1] -= 1

    for cnt in range(n):
        if not students[cnt] and cnt - 1 != 0 and students[cnt - 1] == 2:
            students[cnt - 1] -= 1
            students[cnt] += 1

        if not students[cnt] and cnt + 1 != n and students[cnt + 1] == 2:
            students[cnt + 1] -= 1
            students[cnt] += 1
    # print(students)

    count = 0
    for student in students:
        if student:
            count += 1


    return count










result = solution(5, [2, 4], [1, 3, 5])
print(result)

result = solution(5, [2, 4], [3])
print(result)