import sys
sys.stdin = open("5648_input.txt")


def find_location(x, y, direction):
    if direction == 0:
        return x, y + 1
    if direction == 1:
        return x, y - 1
    if direction == 2:
        return x - 1, y
    return x + 1, y


T = int(input())
for tc in range(T):
    N = int(input())
    data = list()
    result = 0
    for i in range(N):
        temp = list(map(int, input().split()))
        # 0.5에서 소멸하는 경우를 막기 위해 2배
        temp[0] *= 2
        temp[1] *= 2
        data.append(temp)
    # Map의 크기가 -2000에서 2000까지 == 4002회
    for roop in range(4002):
        Map = dict()
        conut = 0
        for i in range(N):
            if not data[i]:
                conut += 1
                continue
            new_x, new_y = find_location(data[i][0], data[i][1], data[i][2])
            if new_x < -2000 or new_x > 2000 or new_y < -2000 or new_y > 2000:
                data[i] = []
                continue
            data[i][0] = new_x
            data[i][1] = new_y
            if Map.get((new_x, new_y)):
                Map[(new_x, new_y)].append(i)
            else:
                Map[(new_x, new_y)] = [i]

        if conut == N:
            break

        for key, value in Map.items():
            if len(value) > 1:
                for index in value:
                    result += data[index][3]
                    data[index] = []

    print(f"#{tc + 1} {result}")