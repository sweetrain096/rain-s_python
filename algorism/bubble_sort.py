def BubbleSort(data) :
    for i in range(len(data) - 1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

data = [2, 4, 1, 3, 5]

BubbleSort(data)
print(data)