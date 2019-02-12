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




# result = solution(["leo", "kiki", "eden"], ["eden", "kiki"])  # "leo"
# result = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])    # "vinko"
result = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])     # "mislav"


# result = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])    # "vinko"
print(result)