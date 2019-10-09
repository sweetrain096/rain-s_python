skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0
    for now_skill in skill_trees:
        index = 0
        flag = 0
        for now in now_skill:
            if skill[index] == now:
                index += 1
            elif now not in skill:
                continue
            else:
                flag = 1
                break
            if index == len(skill):
                break
        if not flag:
            answer += 1

    return answer

print(solution(skill, skill_trees))