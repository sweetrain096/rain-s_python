def selection_sort(data):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]

data = [4, 6, 3, 7, 8, 1, 9, 5, 2]
selection_sort(data)
print(data)