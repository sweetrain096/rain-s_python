def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1. divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 리스트의 길이가 1이 될 때 까지 divide
    left = merge_sort(left)
    right = merge_sort(right)

    # merge 부분
    return merge(left, right)



def merge(left, right):
    # 복사할 임시 배열
    result = []

    # 양쪽 두 리스트 중 하나라도 원소가 없을 때 까지 반복
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # 만약 왼쪽 혹은 오른쪽 리스트가 남았을 때
    # 모두 다 집어넣기
    if left:
        result.extend(left)
    elif right:
        result.extend(right)

    return result


data = [61, 324, 21, 56, 243, 6, 1, 634, 43, 3, 52]
print(merge_sort(data))