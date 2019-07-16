# arr = [1, 2, 4, 7, 8, 3]
# arr = [6, 6, 7, 7, 6, 7]
arr = [0, 5, 4, 0, 6, 0]

def babyGin():
    global flag
    triple, run, tmp = 0, 0, 0
    for i in range(2):
        if arr[i] == arr[i + 1]:
            triple += 1
        elif arr[i] == arr[i + 1] + 1:
            run += 1
    if triple == 2 or run == 2:
        tmp += 1

    if tmp:
        triple, run = 0, 0
        for i in range(3, 5):
            if arr[i] == arr[i + 1]:
                triple += 1
            elif arr[i] == arr[i + 1] + 1:
                run += 1
        if triple == 2 or run == 2:
            tmp += 1

    if tmp == 2:
        flag = 1
        return

    return

def perm(n, k):
    if n == k:
        # print(arr)
        babyGin()
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k + 1)
            arr[i], arr[k] = arr[k], arr[i]
    return


flag = 0
perm(6, 0)


if flag:
    print("BabyGin")
else:
    print("Not babyGin")