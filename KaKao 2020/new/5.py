def is_build(x, y, a, b, data):
    if b:  # 설치할 때
        if a:  # 보
            if data.get((x, y-1)):  # 왼쪽이 기둥과 연결
                if 0 in data[(x, y-1)]:
                    return True
            if data.get((x + 1, y - 1)):    # 오른쪽이 기둥과 연결
                if 0 in data[(x+1, y-1)]:
                    return True
            if data.get((x-1, y)) and data.get((x+1, y)):   # 좌우 보 연결
                if 1 in data[(x-1, y)] and 1 in data[(x+1, y)]:
                    return True

            return False
        # 기둥은 바닥위, 보 한쪽 끝, 다른 기둥 위
        else:  # 기둥
            if not y:   # 바닥에 설치될 때
                return True
            if data.get((x, y-1)):  # 기둥 위에 설치될 때
                if 0 in data[(x, y-1)]:
                    return True
            if data.get((x-1, y)):  # 보의 오른쪽 끝
                if 1 in data[(x-1, y)]:
                    return True
            if data.get((x, y)):    # 보의 왼쪽 끝
                if 1 in data[(x, y)]:
                    return True
            return False


    else:   # 삭제할 때
        if a:   # 보
            # 보의 왼쪽 오른쪽 보 연결 체크
            # 연결된 보의 좌 우 기둥 없을 경우 삭제 불가
            if data.get((x-1, y)) and 1 in data[(x-1, y)]:  # 왼쪽
                if not data.get((x - 1, y - 1)) and not data.get((x, y - 1)):
                    return False
                if data.get((x-1, y-1)) or data.get((x, y-1)): # 연결기둥
                    if 0 in data[(x-1, y-1)] or 0 in data[(x, y-1)]:
                        return False
            # print(x, y)
            if data.get((x+1, y)) and 1 in data[(x+1, y)]:  # 오른쪽
                if not data.get((x+1, y-1)) and not data.get((x+2, y-1)):
                    return False
                if data.get((x+1, y-1)) or data.get((x+2, y-1)):
                    print("in")
                    if 0 in data[(x+1, y-1)] or 0 in data[(x+2, y-1)]:
                        return False

            return True
        else:   # 기둥
            if not y:   # 바닥에 설치한 경우 삭제 가능
                return True
            if data.get((x, y+1)):  # 기둥 위에 설치물 있을 경우 삭제 불가
                return False
            if data.get((x-1, y+1)):    # 기둥 위 보 있을 경우 삭제 불가
                if 1 in data[(x-1, y+1)]:
                    return False

            return True



def solution(n, build_frame):
    answer = [[]]
    data = dict()
    for order in build_frame:
        x, y, a, b = order
        if not is_build(x, y, a, b, data):
            continue


        # 조건을 맞췄을 경우 dict에 추가

        if b:
            if data.get((x, y)):
                data[(x, y)].append(a)
            else:
                data[(x, y)] = [a]
        else:
            if len(data[(x, y)]) == 2:
                data[(x, y)].pop(a)
            elif len(data[(x, y)]) == 1:
                data.pop((x, y))
        # print(data)
    data_list =[]
    for key, val in data.items():
        # print(key, val)
        data_list.append([key[0], key[1], val[0]])
    # print(data_list)
    answer = sorted(data_list)
    return answer


NS = [5, 5]
BUILDS = [[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	,
          [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	]


for i in range(len(NS)):
    print(solution(NS[i], BUILDS[i]))