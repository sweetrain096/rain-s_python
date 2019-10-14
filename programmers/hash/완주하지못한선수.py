# participant = 	['leo', 'kiki', 'eden']
# completion = ['eden', 'kiki']
# participant = 	['marina', 'josipa', 'nikola', 'vinko', 'filipa']
# completion = ['josipa', 'filipa', 'marina', 'nikola']
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

def solution(participant, completion):
    answer = ""
    data = dict()
    for i in participant:
        if not data.get(i):
            data[i] = 1
        else:
            data[i] += 1

    for j in completion:
        if data.get(j) == 1:
            data.pop(j)
        else:
            data[j] -= 1

    for k in data:
        answer += k
    return answer


print(solution(participant, completion))


















'''
def solution(participant, completion):
    if len(set(participant)) == len(participant):
        answer = list(set(participant) - set(completion))[0]

    else:
        plus = 0
        participant.sort()
        completion.sort()
        for cnt in range(len(completion)):
            if participant[cnt] != completion[cnt]:
                return participant[cnt]
            if cnt == len(completion) - 1:
                return participant[-1]

    return answer
'''