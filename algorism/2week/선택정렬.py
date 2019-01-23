def selection_sort(a):
    for i in range(0, len(a)-1):
        min_check = i
        for j in range(i + 1, len(a)):
            if a[min_check] > a[j]:
                min_check = j
        a[i], a[min_check] = a[min_check], a[i]

data = [64, 25, 10, 22, 11]
print(data)
selection_sort(data)
print(data)
