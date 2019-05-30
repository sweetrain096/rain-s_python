def merge_sort(m):
    if len(m) <= 1:
        return m

    # 1. divide
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 리스트 길이가 1이 될 때 까지 divide
    left = merge_sort(left)
    right = merge_sort(right)

    # merge 부분
    return merge(left, right)

def merge(left, right):
    result = []
    # 양 쪽 리스트에 원소가 없을 때 까지 반복
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    elif right:
        result.extend(right)
    return result


data = [61, 324, 21, 56, 243, 6, 1, 634, 43, 3, 52]
print(data)
print(merge_sort(data))