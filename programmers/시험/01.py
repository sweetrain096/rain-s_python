n = int(input())

t = int(n ** 0.5)
flag = False
result = 99999999999999999

for w in range(t, n + 1):
    for h in range(n - t + 1, 0, -1):
        if w * h == n:
            result = min(result, abs(w-h))
            flag = True
            break
    if flag:
        break

print(result)