def binary_search(a, key):
    start = 0
    end = len(a) - 1
    while start <= end :
        middle = (start + end) // 2
        if key == a[middle]: # 검색 성공
            return middle
        elif key < a[middle] :
            end = middle - 1
        else :
            start = middle + 1


key = 22
data = [2, 4, 7, 9, 11, 19, 23]
print("index", binary_search(data, key))