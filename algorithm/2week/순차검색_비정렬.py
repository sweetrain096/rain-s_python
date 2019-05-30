def sequential_search(a, n, key):
    # i = 0
    # while i < n and a[i] != key:
    #     i += 1
    #     if i < n :
    #         return i
    #     else :
    #         return None


    for i in range(n):
        if a[i] == key:
            return i
    return None


data=[4, 9, 11, 23, 2, 19, 7]
key = 19

print("index", sequential_search(data, len(data), key))

