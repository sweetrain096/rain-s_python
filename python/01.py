n_count = int(input())
for number in range(n_count) :
    strings = input()
    check_string = strings[0]
    cnt = 0
    while True:
        cnt += 1
        if not strings.strip(check_string):
            print(check_string)
            break
        else :
            check_string += strings[0 + cnt]

    print(f"#{number+1} {len(check_string)}")

