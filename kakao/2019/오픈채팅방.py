def solution(record):
    users = dict()
    result = []
    answer = []
    for line in record:
        data = line.split()
        order, user_id = data[0], data[1]
        if len(data) == 3:
            nickname = data[2]
            users[user_id] = nickname
        if order[0] == 'C':
            continue
        result.append([user_id, order])

    for i in result:
        temp = users[i[0]]+'님이 '
        if i[1][0] == 'E':
            temp += '들어왔습니다.'
        else:
            temp += '나갔습니다.'
        answer.append(temp)
    return answer



RECORD = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(RECORD))