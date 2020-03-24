def solution(s):
    s_list = []
    tmp = []
    temp_int = ""
    for i in range(len(s)):
        if s[i] == '{':
            continue
        elif s[i] == '}':
            if temp_int:
                tmp.append(int(temp_int))
                s_list.append(tmp)
                tmp = []
                temp_int = ""
        elif s[i] == ',':
            if temp_int:
                tmp.append(int(temp_int))
                temp_int = ""
        else:
            temp_int += s[i]
    s_list = sorted(s_list, key=len)
    answer = []
    for i in s_list:
        if len(i) == 1:
            answer.append(i[0])
        else:
            for j in i:
                if j not in answer:
                    answer.append(j)

    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))