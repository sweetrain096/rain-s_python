def insertion_sort(data):
    for i in range(1, len(data)):   # 현재 바꿀 index == i
        j = i-1         # 바꿀 인덱스보다 한 칸 앞
        key = data[i]   # 바꿀 인덱스의 요소값
        while data[j] > key and j >= 0:
        # 이미 정렬된 인덱스가 현재 값보다 크고, 가리키는 인덱스가 0보다 크거나 같을때
            data[j+1] = data[j]     # 계속해서 data는 한칸씩 뒤로 밀린다.
            j -= 1                  # 인덱스 값을 하나씩 앞으로 당긴다.
        data[j+1] = key             # while문 탈출시 빈 칸에 key값 넣기

data = [3, 5, 2, 6, 7, 1, 4]
insertion_sort(data)
print(data)