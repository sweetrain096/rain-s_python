import sys
sys.stdin = open("5550_input.txt")

right = "croak"

for tc in range(int(input())):
    data = [0, 0, 0, 0, 0]
    able = [0 for _ in range(500)]
    cnt = 0
    input_data = input()
    for char in input_data:
        if cnt == -1:
            break
        for i in range(5):
            if not i:
                if char == right[i]:
                    data[i] += 1
                    if not cnt:
                        able[cnt] = 1
                        cnt += 1
                    else:
                        flag = False
                        for j in range(cnt):
                            if not able[j]:
                                able[j] = 1
                                flag = True
                                break
                        if not flag:
                            able[cnt] = 1
                            cnt += 1
                    break
            else:
                if char == right[i]:
                    if data[i - 1] > data[i]:
                        data[i] += 1
                        if i == 4:
                            for j in range(cnt):
                                if able[j]:
                                    able[j] = 0
                                    break
                    else:
                        cnt = -1
                        break
                    break
    # print(data)
    if data[0] != data[-1]:
        cnt = -1
    print(f"#{tc + 1} {cnt}")