def solution(stones, k):
    answer = 0
    n = len(stones)
    checked = [0 for _ in range(n)]
    while True:
        Min = min(stones)
        jump = 0
        for i in range(n):
            if checked[i]:
                jump += 1
                if jump >= k:
                    return answer
            else:
                jump = 0
                stones[i] -= Min
                if stones[i] == 0:
                    checked[i] = 1
                    stones[i] = 200000000
        answer += Min


    return answer



print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))