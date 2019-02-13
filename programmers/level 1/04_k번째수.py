def solution(array, commands):
    answer = []
    for cnt in range(len(commands)):
        i, j, k = commands[cnt]

        answer.append(sorted(array[i - 1 : j])[k - 1])

    return answer


result = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(result)