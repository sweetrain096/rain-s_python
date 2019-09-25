import sys
sys.stdin = open("3820_input.txt")

def merge_sort(div_list):
    if len(div_list) <= 1:
        return div_list
    mid = len(div_list) // 2
    left = div_list[:mid]
    right = div_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if (left[0][0]-1)*right[0][1] >= (right[0][0]-1)*left[0][1]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    elif right:
        result.extend(right)
    return result

for tc in range(int(input())):
    n = int(input())
    data = []
    for i in range(n):
        a, b = map(int, input().split())
        data.append([a, b])
    sort_data = merge_sort(data)

    v = 1
    for i in sort_data:
        v = i[0]*v + i[1]
    print(f"#{tc+1} {v%1000000007}")