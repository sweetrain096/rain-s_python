n = int(input())

for i in range(n) :
    x, y = map(int, input().split(" "))
    k = 1
    cnt = 0
    while True :
        x += k
        y -= k
        cnt += 2
        if y - x == k  or y - x == k + 1 :
            cnt += 1
            break
        elif y - x == 2 * k  + 1  or y - x == 2 * (k + 1):
            cnt += 2
            break
        else :
            k += 1

    print(cnt)
