def solution(k, room_number):
    answer = []
    temp_Max = 1
    rooms = [0 for _ in range(k)]
    for i in room_number:
        if not rooms[i-1]:
            rooms[i-1] = 1
            answer.append(i)
            if temp_Max == i:
                temp_Max += 1
        else:
            if i < temp_Max:
                rooms[temp_Max-1] = 1
                answer.append(temp_Max)
                for j in range(temp_Max + 1, k):
                    if not rooms[j-1]:
                        temp_Max = j
                        break
            else:
                for j in range(i+1, k):
                    if not rooms[j-1]:
                        rooms[j-1] = 1
                        answer.append(j)

    return answer


print(solution(10, [1,3,4,1,3,1]))