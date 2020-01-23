import sys
sys.stdin = open("7588_input.txt")

for tc in range(int(input())):
    n = int(input())
    NumDict = dict()
    print(f"#{tc + 1}")
    for line in range(n):
        temp = list(map(int, input().split()))
        type = temp[0]
        if type == 1:
            a, b = temp[1], temp[2]
            NumDict[line + 1] = (a, b)
        elif type == 2:
            i = temp[1]
            if NumDict.get(i):
                NumDict.pop(i)
        else:
            x = temp[1]
            Max = 0
            flag = False
            for i in range(1, n+1):
                if NumDict.get(i):
                    a, b = NumDict[i]
                    Max = a * x + b
                    flag = True
                    break
            if not flag:
                print("NO")
                continue
            if x > 0:
                arr = list(NumDict.values())
                if len(arr) > 100:
                    sortA = sorted(arr, reverse=True)
                    MaxA = sortA[0][0] * x + sortA[0][1]
                    for a1, b1 in sortA:
                        if MaxA < a1 * x + b1:
                            MaxA = a1 * x + b1

                    sortB = sorted(arr, key=lambda Num: Num[1], reverse=True)
                    MaxB = sortB[0][0] * x + sortB[0][1]
                    for a2, b2 in sortB:
                        if MaxB < a2 * x + b2:
                            MaxB = a2 * x + b2
                    if MaxA >= MaxB:
                        print(MaxA)
                    else:
                        print(MaxB)
                else:
                    MaxA = arr[0][0] * x + arr[0][1]
                    for a1, b1 in arr:
                        if MaxA < a1 * x + b1:
                            MaxA = a1 * x + b1
                    print(MaxA)
            else:
                arr = list(NumDict.values())
                if len(arr) > 100:
                    sortA = sorted(arr)
                    MaxA = sortA[0][0] * x + sortA[0][1]
                    for a1, b1 in sortA:
                        if MaxA < a1 * x + b1:
                            MaxA = a1 * x + b1

                    sortB = sorted(arr, key=lambda Num: Num[1], reverse=True)
                    MaxB = sortB[0][0] * x + sortB[0][1]
                    for a2, b2 in sortB:
                        if MaxB < a2 * x + b2:
                            MaxB = a2 * x + b2
                    if MaxA >= MaxB:
                        print(MaxA)
                    else:
                        print(MaxB)
                else:
                    MaxA = arr[0][0] * x + arr[0][1]
                    for a1, b1 in arr:
                        if MaxA < a1 * x + b1:
                            MaxA = a1 * x + b1
                    print(MaxA)
