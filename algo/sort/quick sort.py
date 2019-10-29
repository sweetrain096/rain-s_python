def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    # pivot = arr[0] 도 무관함.
    low = []        # 피봇보다 작음
    high = []       # 피봇보다 큼
    equal = []      # 피봇이랑 같음. 정렬됨
    for i in arr:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        else:
            equal.append(i)
    # 정렬되지 않은 low와 high를 다시 quick sort
    return quick_sort(low) + equal + quick_sort(high)

data = [3, 7, 8, 5, 2, 1, 9, 5, 4]
print(quick_sort(data))

