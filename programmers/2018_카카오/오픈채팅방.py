record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


record_list = []
nicknames = {}

def solution(record):
    for data in record:
        split_data = data.split()
        if split_data[0][0] == 'E':
            record_list.append((split_data[1], 'E'))
            nicknames[split_data[1]] = split_data[2]
        elif split_data[0][0] == 'L':
            record_list.append((split_data[1], 'L'))
        else:
            nicknames[split_data[1]] = split_data[2]

    answer = []
    for i in record_list:
        if i[1] == 'E':
            answer.append(f"{nicknames[i[0]]}님이 들어왔습니다.")
        else:
            answer.append(f"{nicknames[i[0]]}님이 나갔습니다.")

    return answer


print(solution(record))

