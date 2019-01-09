T = int(input())
tests = []


for i in range(T) :
    a, b = map(int, input().split(" "))
    i = 2
    a_mult = 0
    b_sum = b
    while True :
        a_mult = a * i
        if a_mult == b_sum :
            print(a_mult)
            break
        elif a_mult > b_sum :
            b_sum = b_sum + b
        i += 1
