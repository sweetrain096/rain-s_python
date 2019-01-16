n = int(input())

for i in range(n) :
    x, y = map(int, input().split(" "))
    if y - x == 1 :
        print(1)
        break

    print(int(round((y - x) / 2, 0)))
