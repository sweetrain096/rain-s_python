def quick_sort(start, end):
    if start >= end:
        return
    t, p = start, end
    for i in range(start, end + 1):
        # start부터 차례대로 돌면서 end pivot과 비교
        # end pivot이 더 크면
        if arr[i] < arr[p]:
            # start가 있던 위치와 swap
            arr[i], arr[t] = arr[t], arr[i]
            # 변경된 후 위치 +1
            t += 1

    arr[p], arr[t] = arr[t], arr[p]
    quick_sort(start, t-1)
    quick_sort(t+1, end)


arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quick_sort(0, len(arr)-1)
print(arr)