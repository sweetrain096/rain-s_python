n = int(input())

for i in range(n) :
    x, y = map(int, input().split(" "))

    k = 1
    cnt = 0
    count = 0
    while True :
        count += 1
        if y - x == 1 :
            cnt += 1
            break
        if y - x == 2:
            cnt += 2
            break
        x += k
        y -= k
        print(k)
        print(x, y)
        cnt += 2
        if y - x == k  or y - x == k + 1 or y - x == k - 1:
            cnt += 1
            break
        elif y - x == 2 * k  + 1  or y - x == 2 * (k + 1) or y - x == 2 * k or y - x == 2 * k - 1:
            cnt += 2
            break
        else :
            k += 1

        if count == 11 :
            break
    print(cnt)
