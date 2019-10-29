def heapify(arr, index, heap_size):
    # 완전이진트리는 배열 하나로 트리 구현가능
    largest = index
    left = index * 2 + 1    # 왼쪽 자식
    right = index * 2 + 2   # 오른쪽 자식
    # 왼쪽 자식이 현재 요소보다 크면 인덱스 교체
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    # 오른쪽 자식이 현재 요소보다 크면 인덱스 교체
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    # 교체된적이 있다면 교체된 index와 largest 요소값 교체
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        # 변경되었으면 변경된 부분을 중심으로 다시 한번 heapify
        heapify(arr, largest, heap_size)


def heap_sort(arr):
    n = len(arr)

    # 최초 힙
    # 트리의 절반부터 거꾸로 올라가며 heapify를 하는것이 효율적
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    # 한번 구성된 힙을 정렬.
    # 가장 큰 값(루트) 를 가장 끝 값으로 이동한 후 힙 생성.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr


data = [61, 324, 21, 56, 243, 6, 1, 634, 43, 3, 52]
print(heap_sort(data))
