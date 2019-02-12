def solution(answers):
    answer = []
    total = len(answers)
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    sums = [0, 0, 0]


    if total > len(first):
        first *= total // len(first) + 1
    if total > len(second):
        second *= total // len(second) + 1
    if total > len(third):
        third *= total // len(third) + 1

    plus = 0
    for check in answers:
        if check == first[plus]:
            sums[0] += 1
        if check == second[plus]:
            sums[1] += 1
        if check == third[plus]:
            sums[2] += 1
        plus += 1

    max_sum = -1
    for check in range(3):
        if max_sum < sums[check]:
            max_sum = sums[check]


    for check in range(3):
        if max_sum == sums[check]:
            answer.append(check + 1)


    return answer


# answer = solution([3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5])
# [3]
# answer = solution([1, 2, 3, 4, 5])
# [1]

answer = solution([1, 2, 3, 4, 5])
print(answer)