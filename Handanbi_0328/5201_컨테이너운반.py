import sys
sys.stdin = open("5201_input.txt")

for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    for i in range(n - 1):
        for j in range(i + 1, n):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    for i in range(m - 1):
        for j in range(i + 1, m):
            if truck[i] < truck[j]:
                truck[i], truck[j] = truck[j], truck[i]
    # print(data)
    # print(truck)

    cnt_data, cnt_truck, result = 0, 0, 0
    while cnt_data < n and cnt_truck < m:
        if truck[cnt_truck] >= data[cnt_data]:
            result += data[cnt_data]
            cnt_truck += 1
            cnt_data += 1
        else:
            cnt_data += 1

    print("#{} {}".format(tc + 1, result))