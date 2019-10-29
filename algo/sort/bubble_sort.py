def bubble_sort(data):
    for i in range(len(data) - 1, 0, -1):
        print(len(data)-i, "turn")
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # swap
                print(f"{data} index {j}, {j+1} swap")
            else:
                print(data)

data = [2, 4, 1, 3, 5]
bubble_sort(data)
print(data)