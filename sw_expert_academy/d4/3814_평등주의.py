import sys
sys.stdin = open("3814_input.txt")

for tc in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    errors = [[0, 0] for _ in range(n)]
    c = 0
    second = 0
    for i in range(n):
        if i == 0:
            errors[i][1] = abs(data[i + 1] - data[i])
        elif i == n-1:
            errors[i][0] = abs(data[i-1] - data[i])
        else:
            errors[i][0] = abs(data[i] - data[i-1])
            errors[i][1] = abs(data[i+1] - data[i])
        if errors[i][0] > c:
            second = c
            c = errors[i][0]
        if errors[i][1]>c:
            second = c
            c = errors[i][1]

    while (1):
        min_value = c - second
        if k < min_value:
            continue
        else:
            for i in range(n):
                if errors[i][0] == c:
                    data[i] -= min_value
                    k -= min_value
                    if k <= 0:
                        break
                    if i == 0:
                        errors[i][1] = abs(data[i+1] - data[i])
                    elif i == n-1:
                        errors[i][0] = abs(data[i]-data[i-1])
                    else:
                        errors[i][0] = abs(data[i+1]-data[i])
                        errors[i][1] = abs(data[i]-data[i-1])
                if errors[i][1] == c:
                    data[i] -= min_value
                    k -= min_value
                    if k <= 0:
                        break
                    if i == 0:
                        errors[i][1] = abs(data[i + 1] - data[i])
                    elif i == n - 1:
                        errors[i][0] = abs(data[i] - data[i - 1])
                    else:
                        errors[i][0] = abs(data[i + 1] - data[i])
                        errors[i][1] = abs(data[i] - data[i - 1])
            c, second = 0, 0
            for i in range(n):
                if errors[i][0]>c:
                    second = c
                    c = errors[i][0]
                if errors[i][1]>c:
                    second = c
                    c = errors[i][1]

    print(errors, c)