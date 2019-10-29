def counting_sort(data, count, result):
    for i in data:
        count[i] += 1   # data 요소의 출현 횟수
    print("count", count)

    for i in range(len(count)-1):
        count[i+1] += count[i]  # 누적 count
    print("누적 count", count)

    for i in range(len(data)-1, -1, -1):
        result[count[data[i]] - 1] = data[i]
        count[data[i]] -= 1
        print("result", result, "count", count)



data = [3, 2, 5, 4, 2, 1, 5, 2, 2, 1]
count = [0 for _ in range(max(data)+1)]   # 최댓값
result = [0 for _ in range(len(data))]  # data 길이만큼
counting_sort(data, count, result)
print(result)