N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

# N = 4
# stages = [4, 4, 4, 4, 4]


def solution(N, stages):
    total = len(stages)
    stage_list = [0 for _ in range(N + 2)]
    answer = []
    for stage in stages:
        stage_list[stage] += 1
    for stage in range(len(stage_list)):
        now = stage_list[stage]
        stage_list[stage] = now / total
        total -= now
        if total == 0:
            break



    visit = [0 for _ in range(N + 2)]
    while (sum(visit) < N):
        Max = max(stage_list[1:-1])
        if not stage_list[-1]:
            iter_cnt = len(stage_list) - 1
        else:
            iter_cnt = len(stage_list)
        for i in range(1, iter_cnt):
            if not visit[i] and stage_list[i] == Max:
                visit[i] = 1
                answer.append(i)
                stage_list[i] = -1


    print(answer)

    return answer

solution(N, stages)