n_count = int(input())
for number in range(n_count) :
    strings = input()
    check_string = strings[0]
    cnt = 1

    while True:
        quotient = 30 // len(check_string)
        if check_string * quotient == strings[:quotient * len(check_string)]:
            break
        else :
            check_string += strings[cnt]
            cnt += 1
    print(f"#{number+1} {len(check_string)}")