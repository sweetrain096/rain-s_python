# def solution(participant, completion):
#     plus1 = 0
#     for person in participant:
#         plus2 = 0
#         for complet in completion:
#             if person == complet:
#                 participant[plus1] = ""
#                 completion[plus2] = ""
#                 break
#             plus2 += 1
#         plus1 += 1
#
#     answer = ''.join(participant)
#     return answer

def solution(participant, completion):
    if len(set(participant)) == len(participant):
        answer = list(set(participant) - set(completion))[0]

    else:

        plus1 = 0
        for person in participant:
            print(person)
            print(participant)
            print(completion)
            plus2 = 0
            check = 0
            for complete in completion:
                if person == complete:
                    participant[plus1] = ""
                    completion[plus2] = ""
                    break
                plus2 += 1
                check += 1
            if check == len(completion):
                answer = person
                return answer
            plus1 += 1

        answer = ''.join(participant)
    return answer




# result = solution(["leo", "kiki", "eden"], ["eden", "kiki"])  # "leo"
# result = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])    # "vinko"
result = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])     # "mislav"


# result = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])    # "vinko"
print(result)